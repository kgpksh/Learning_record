import math
from datetime import datetime
from tabnanny import check
import torch
from torch import nn
import torch.nn.functional as F
import sqlite3
import collections
import itertools
import random
import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

current_ratio=0
total_value=100
cur_eth_amount=0
rewardss=0
ep=0
fee_ratio=0.00032

minimum_buffer_size=30000
learning_rate = 0.0001
gamma         = 0.9995
buffer_limit  = 300000
batch_size    = 512

def cal(act,nows,nowp,nextp):
    global total_value,cur_eth_amount,rewardss,ep,current_ratio
    
    re=0
    
    if act==75:
        if nows==75:
            re=(nextp-nowp)*cur_eth_amount
        elif nows==-75:
            tgt_eth_amount=math.trunc((((act/100)*total_value)/nowp)*1000)/1000
            re=((nextp-nowp)*tgt_eth_amount)-(-cur_eth_amount+tgt_eth_amount)*nowp*fee_ratio
            cur_eth_amount=tgt_eth_amount
            ep=nowp
        elif nows==0:
            tgt_eth_amount=math.trunc((((act/100)*total_value)/nowp)*1000)/1000
            re=((nextp-nowp)*tgt_eth_amount)-(nowp*tgt_eth_amount*fee_ratio)
            cur_eth_amount=tgt_eth_amount
            ep=nowp

    elif act==-75:
        if nows==-75:
            re=(nextp-nowp)*cur_eth_amount
        elif nows==75:
            tgt_eth_amount=math.trunc((((act/100)*total_value)/nowp)*1000)/1000
            re=((nextp-nowp)*tgt_eth_amount)-(cur_eth_amount-tgt_eth_amount)*nowp*fee_ratio
            cur_eth_amount=tgt_eth_amount
            ep=nowp
        elif nows==0:
            tgt_eth_amount=math.trunc((((act/100)*total_value)/nowp)*1000)/1000
            re=(nextp-nowp)*tgt_eth_amount+(nowp*tgt_eth_amount*fee_ratio)
            cur_eth_amount=tgt_eth_amount
            ep=nowp
    
    elif act==0 :
        if nows==75:
            re=-(nowp*cur_eth_amount*fee_ratio)
            cur_eth_amount=0
        elif nows==-75:
            re=nowp*cur_eth_amount*fee_ratio
            cur_eth_amount=0

    elif act==0 and nows==0:
        re=0
        ep=0

    if not total_value==0:
        rewardss=re*100/total_value
    else: rewardss=0

    current_ratio=act

    total_value=total_value+re
    


train_path='D:/Documents/CODING/Binance_RL_Bot/min_candle/for_train4.db'
con=sqlite3.connect(train_path)
sql='SELECT "O","H","L","C","V","Mean_Price","trade_num","buyer_ratio" FROM eth_1min_kline'
cursor=con.cursor()
cursor.execute(sql)
rows=cursor.fetchall()
con.close()
# conn=sqlite3.connect('D:/Documents/CODING/Binance_RL_Bot/2nd_cost.db')
class Qnet(nn.Module):
    def __init__(self):
        super(Qnet, self).__init__()
        # self.model=nn.Sequential(
        #     nn.Linear(2162,256),
        #     nn.ReLU(),
        #     nn.Linear(256,256),
        #     nn.ReLU(),
        #     nn.Linear(256,256),
        #     nn.ReLU(),
        #     nn.Linear(256,256),
        #     nn.ReLU(),
        #     nn.Linear(256,10)
        # )
        self.fc1 = nn.Linear(2162, 256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 256)
        self.fc4 = nn.Linear(256, 256)
        self.fc5 = nn.Linear(256,3)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.fc5(x)
        return x
      
    def sample_action(self, obs, epsilon):
        out = self.forward(obs)
        coin = random.random()
        if coin < epsilon:
            return random.randint(0,2)
        else : 
            return out.argmax().item()
            
def train(q, q_target, memory, optimizer):
    for i in range(15):
        s,a,r,s_prime,done= memory.sample(batch_size)

        q_out = q(s)
        q_a = q_out.gather(1,a)
        max_q_prime = q_target(s_prime).max(1)[0].unsqueeze(1)
        target = r + gamma * max_q_prime*done
        loss = F.smooth_l1_loss(q_a, target).to(device)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()  
        


# class state():
#     def __init__(self,min,ratio,gap):
#         super().__init__()
#         self.slice=torch.Tensor(rows[min:min+180]).to(device)
#         self.fst=self.slice[:,0:4]*100/self.slice[0][0:4]
#         self.merge=torch.cat([self.slice,self.fst],dim=1)
#         self.last=torch.Tensor([ratio,gap]).to(device)
    
#     def output(self):
#         final=torch.cat([self.merge.view(-1,1).squeeze(),self.last])
#         return final

def supplyer(min,ratio,gap):
    slice=torch.Tensor(rows[min:min+180]).to(device)
    fst=slice[:,0:4]*100/slice[0][0:4]
    merge=torch.cat([slice,fst],dim=1)
    last=torch.Tensor([ratio,gap]).to(device)
    return torch.cat([merge.view(-1,1).squeeze(),last])

class ReplayBuffer():
    def __init__(self):
        self.buffer = collections.deque(maxlen=buffer_limit)
    
    def put(self, transition):
        self.buffer.append(transition)
    
    def sample(self, n):
        mini_batch = random.sample(self.buffer, n)
        s_lst, a_lst, r_lst, s_prime_lst, done_lst = [], [], [], [], []
        
        for transition in mini_batch:
            s, a, r, s_prime, is_done= transition
            s_lst.append(torch.from_numpy(s).to(device))
            a_lst.append([a])
            r_lst.append([r])
            s_prime_lst.append(torch.from_numpy(s_prime).to(device))
            done_lst.append([is_done])
         

        return torch.stack(s_lst).to(device), \
            torch.tensor(a_lst).to(device),\
            torch.tensor(r_lst,dtype=torch.float).to(device), \
            torch.stack(s_prime_lst).to(device), \
            torch.tensor(done_lst).to(device)
    
    def size(self):
        return len(self.buffer)
        
# q = Qnet().to(device)
q=Qnet().to(device)
checkpoint=torch.load('D:/Documents/CODING/Binance_RL_Bot/models/model_checkpoint_2/4.861873830399604_2180.tar')
q.load_state_dict(checkpoint['model_state_dict'])
q.train()
q_target = Qnet().to(device)
q_target.load_state_dict(q.state_dict())
memory = ReplayBuffer()
print_interval = 10
optimizer = optim.Adam(q.parameters(), lr=learning_rate)
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])


for epoch in itertools.count():
# for epoch in range(1,120):
    uepoch=epoch+2180
    epsilon = max(0.01, 0.1 - 0.01*(uepoch/300)) #Linear annealing from 8% to 1%

    current_ratio=0
    total_value=100
    cur_eth_amount=0
    rewardss=0
    ep=0
    now_state=supplyer(0,0,0)
    # next_state=0
    isliquidated=False

    for minute in range(1,292140):
        # if minute%1000==0:
        #     print(str(minute)+'/299340')
        #     print(datetime.now())

        now_price=rows[minute+179][3]
        next_price=rows[minute+180][3]
        action=q.sample_action(now_state,epsilon)

        if action==1:
            act=75
        elif action==2:
            act=-75
        elif action==0:
            act=0

        cal(act,current_ratio,now_price,next_price)

        if cur_eth_amount>0 and next_price-ep<0 and abs(next_price-ep)*cur_eth_amount/total_value>0.045:     
            isliquidated=True
        elif cur_eth_amount<0 and ep-next_price<0 and abs(ep-next_price)*cur_eth_amount/total_value>0.045:
            isliquidated=True

        if cur_eth_amount>0 :
            next_state=supplyer(minute,current_ratio,(next_price-ep)*cur_eth_amount/total_value*1000)
        elif cur_eth_amount<0:
            next_state=supplyer(minute,current_ratio,(ep-next_price)*cur_eth_amount/total_value*1000)
        elif cur_eth_amount==0:
            next_state=supplyer(minute,current_ratio,0)

        if isliquidated==True:
            rewardss=-100
            total_value=0
            memory.put((now_state.cpu().numpy(),action,rewardss,next_state.cpu().numpy(),0))
            break

        if total_value<5 and cur_eth_amount==0:
            memory.put((now_state.cpu().numpy(),action,rewardss,next_state.cpu().numpy(),0))
            break

        memory.put((now_state.cpu().numpy(),action,rewardss,next_state.cpu().numpy(),1))
        now_state=next_state

    print(str(datetime.now())+'  epoch : '+str(uepoch)+' total value : '+str(total_value))
    sensor11=datetime.now()
    if memory.size()>minimum_buffer_size:
        train(q, q_target, memory, optimizer)

    if uepoch%print_interval==0 and uepoch!=0:
            q_target.load_state_dict(q.state_dict())
            print("Total value : {0}".format(total_value))
            torch.save(q,'D:/Documents/CODING/Binance_RL_Bot/models/model_all_2/{}'.format(str(total_value)+'_'+str(uepoch)+'.pt'))
            # torch.save(q.state_dict(),'D:/Documents/CODING/Binance_RL_Bot/models/model_save_use_2/{}'.format(str(total_value)+'_'+str(epoch)+'.pt'))
            torch.save(
                {'model_state_dict': q.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'epoch' : uepoch}
                ,'D:/Documents/CODING/Binance_RL_Bot/models/model_checkpoint_2/{}'.format(str(total_value)+'_'+str(uepoch)+'.tar')
            )