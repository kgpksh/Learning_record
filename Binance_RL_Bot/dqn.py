from math import gamma
import pprint
from turtle import forward
from torch import nn
import torch
import gym
from collections import deque
import itertools
import numpy as np
import random
import math
import torch.nn.functional as F

GAMMA=0.75
BATCH_SIZE=64
BUFFER_SIZE=50000
MIN_REPLAY_SIZE=1000
EPSILON_START=1.0
EPSILON_END=0.02
EPSILON_DECAY=10000
TARGET_UPDATE_FREQ=1000
EPS_DECAY=200

class Network(nn.Module):
    def __init__(self,env):
        super().__init__()
        in_features=int(np.prod(env.observation_space.shape))
        self.net=nn.Sequential(
            nn.Linear(in_features,256),
            nn.ReLU(),
            nn.Linear(256,env.action_space.n)
        )

    def forward(self, x):
        return self.net(x)

    def act(self, obs):
        obs_t=torch.as_tensor(obs, dtype=torch.float32)
        q_values=self(obs_t.unsqueeze(0))
        max_q_index=torch.argmax(q_values, dim=1)[0]
        # print(max_q_index=torch.argmax(q_values, dim=1))
        action=max_q_index.detach().item()
        # print('action : ')
        # print(action)
        return action

env=gym.make('CartPole-v0')
replay_buffer=deque(maxlen=BUFFER_SIZE)
rew_buffer=deque([0.0],maxlen=100)

episode_reward=0.00

online_net=Network(env)
target_net=Network(env)
optimizer=torch.optim.Adam(online_net.parameters(),lr=5e-4)

target_net.load_state_dict(online_net.state_dict())

obs=env.reset()

step_done=0
for _ in range(MIN_REPLAY_SIZE):
    action=env.action_space.sample()

    new_obs, rew, done, _=env.step(action)
    transition=(obs, action, rew, done, new_obs)
    replay_buffer.append(transition)
    obs=new_obs

    if done:
        obs=env.reset()

for step in itertools.count():
    epsilon=np.interp(step,[0, EPSILON_DECAY], [EPSILON_START, EPSILON_END])
    epsilon=EPSILON_END+(EPSILON_START-EPSILON_END)*math.exp(-1.*step_done/EPS_DECAY)

    rnd_sample=random.random()

    if rnd_sample<=epsilon:
        action=env.action_space.sample()
    else:
        action=online_net.act(obs)

    new_obs, rew, done, _=env.step(action)
    transition=(obs, action, rew, done, new_obs)
    replay_buffer.append(transition)
    obs=new_obs


    episode_reward+=rew

    if done:
        obs=env.reset()

        rew_buffer.append(episode_reward)
        episode_reward=0.0


    transition=random.sample(replay_buffer, BATCH_SIZE)
    # print('1----------------------')
    # print([t[0] for t in transition])

    obses=np.asarray([t[0] for t in transition])
    actions=np.asarray([t[1] for t in transition])
    rews=np.asarray([t[2] for t in transition])
    dones=np.asarray([t[3] for t in transition])
    new_obses=np.asarray([t[4] for t in transition])
    # print('2----------------------')
    # print(obses)

    obses_t=torch.as_tensor(obses,dtype=torch.float32)
    actions_t=torch.as_tensor(actions,dtype=torch.int64).unsqueeze(-1)
    rews_t=torch.as_tensor(rews,dtype=torch.float32).unsqueeze(-1)
    dones_t=torch.as_tensor(dones,dtype=torch.float32).unsqueeze(-1)
    new_obses_t=torch.as_tensor(new_obses,dtype=torch.float32)
    # print('3----------------------')
    # print(obses)

    target_q_values=target_net(new_obses_t)
    max_target_q_values=target_q_values.max(dim=1, keepdim=True)[0]
    targets=rews_t+GAMMA*(1-dones_t)*max_target_q_values

    q_values=online_net(obses_t)
    action_q_values=torch.gather(input=q_values,dim=1, index=actions_t)
    
    nqv=online_net(new_obses_t)
    naqv=nqv.detach().max(1)[0]
    
    print('-----------------------------')
    print('action q values')
    print(nqv)
    print('targets')
    print(naqv)

    loss=nn.functional.smooth_l1_loss(action_q_values, targets)
    # loss=F.mse_loss(action_q_values.squeeze(), naqv)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    step_done+=1
    if step%TARGET_UPDATE_FREQ==0:
        target_net.load_state_dict(online_net.state_dict())

    if step%1000==0:
        print()
        print('Step',step)
        print('Avg Rew',np.mean(rew_buffer))