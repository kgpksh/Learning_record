import gym
import random
import math
import numpy
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from collections import deque
import matplotlib.pyplot as plt
import numpy as np

EPISODES=300
EPS_START=0.9
EPS_END=0.05
EPS_DECAY=200
GAMMA=0.75
LR=0.001
BATCH_SIZE=64
trying=0

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
class DQNAgent():
    def __init__(self):
        self.model=nn.Sequential(
            nn.Linear(4,256),
            nn.ReLU(),
            nn.Linear(256,2)
        ).to(device)
        self.optimizer=optim.Adam(self.model.parameters(),LR)
        self.step_done=0
        self.memory=deque(maxlen=10000)

    def memorize(self, state, action, reward, next_state):
        self.memory.append((
            state,
            action,
            torch.FloatTensor([reward]),
            torch.FloatTensor([next_state])))

    def act(self, state):
        if trying>150:
            eps_threshold=0
        else:
            eps_threshold=EPS_END+(EPS_START-EPS_END)*math.exp(-1.*self.step_done/EPS_DECAY)
        self.step_done+=1
        if random.random()>eps_threshold:
            return self.model(state).data.max(1)[1].view(1,1)
        else:
            return torch.LongTensor([[random.randrange(2)]]).to(device)

    def learn(self):
        if len(self.memory)<BATCH_SIZE:
            return
        batch=random.sample(self.memory,BATCH_SIZE)
        states,actions,rewards,next_states=zip(*batch)

        states=torch.cat(states).to(device)
        actions=torch.cat(actions).to(device)
        rewards=torch.cat(rewards).to(device)
        next_states=torch.cat(next_states).to(device)

        current_q=self.model(states).gather(1,actions)
        max_next_q=self.model(next_states).detach().max(1)[0]
        # print('111=========================================')
        # print(self.model(states))
        # print('222=========================================')
        # print(self.model(states).gather(1,actions))
        # print('333=========================================')
        # print(self.model(states).gather(1,actions).squeeze())
        expected_q=rewards+(GAMMA*max_next_q)
        

        loss=F.mse_loss(current_q.squeeze(),expected_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


env=gym.make('CartPole-v0')
agent=DQNAgent()
target=DQNAgent()
score_history=[]

for e in range(1,EPISODES+1):
    state=np.array(env.reset())
    steps=0
    while True:
        # env.render()
        state=torch.FloatTensor([state]).to(device)

        action=agent.act(state)
        next_state, reward, done, _=env.step(action.item())

        if done:
            reward=-1

        agent.memorize(state, action, reward, next_state)
        agent.learn()

        state=next_state
        steps+=1

        if done:
            print('에피소드 : {0}  점수 : {1}'.format(e,steps))
            score_history.append(steps)
            trying+=1
            break

plt.plot(score_history)
plt.ylabel('score')
plt.show()

