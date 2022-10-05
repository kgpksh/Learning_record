import math
from datetime import datetime
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
cur_usdt_amount=100
cur_eth_amount=0
cur_eth_value=0
rewardss=0
ep=0
fee_ratio=0.00032

minimum_buffer_size=30000
learning_rate = 0.0005
gamma         = 0.9995
buffer_limit  = 300000
batch_size    = 512

def rewarding(act, now_p, next_p):
    global total_value, current_ratio,cur_usdt_amount,cur_eth_amount,cur_eth_amount,rewardss,cur_eth_value,ep
    rewards=0
    
    if act<0:
        tgt_eth_amount=cur_eth_amount
    else:
        tgt_eth_amount=math.trunc((((act/100)*total_value)/now_p)*1000)/1000

    net_cng_amt=tgt_eth_amount-cur_eth_amount
    
    if tgt_eth_amount>0 and cur_eth_amount>0:
        
        if net_cng_amt>0:
            rewards=((next_p-now_p)*tgt_eth_amount)-(now_p*net_cng_amt*fee_ratio)
            ep=(cur_eth_value+net_cng_amt*now_p)/tgt_eth_amount
        elif net_cng_amt<0:
            rewards=((next_p-now_p)*tgt_eth_amount)+(now_p*net_cng_amt*fee_ratio)
            ep=(cur_eth_value+net_cng_amt*now_p)/tgt_eth_amount
        elif net_cng_amt==0:
            rewards=(next_p-now_p)*tgt_eth_amount

    elif tgt_eth_amount>0 and cur_eth_amount<0:
        rewards=((next_p-now_p)*tgt_eth_amount)-(now_p*net_cng_amt*fee_ratio)
        ep=now_p


    elif tgt_eth_amount<0 and cur_eth_amount>0:
        rewards=((next_p-now_p)*tgt_eth_amount)+(now_p*net_cng_amt*fee_ratio)
        ep=-now_p


    elif tgt_eth_amount<0 and cur_eth_amount<0:

        if net_cng_amt>0:
            rewards=((next_p-now_p)*tgt_eth_amount)-(now_p*net_cng_amt*fee_ratio)
            ep=(cur_eth_value-net_cng_amt*now_p)/tgt_eth_amount
        elif net_cng_amt<0:
            rewards=((next_p-now_p)*tgt_eth_amount)+(now_p*net_cng_amt*fee_ratio)
            ep=(cur_eth_value+net_cng_amt*now_p)/tgt_eth_amount
        elif net_cng_amt==0:
            rewards=(next_p-now_p)*tgt_eth_amount

    elif tgt_eth_amount==0 or cur_eth_amount==0:
        
        if tgt_eth_amount>0:
            rewards=(next_p-now_p)*tgt_eth_amount-(now_p*tgt_eth_amount*fee_ratio)
            ep=now_p
        elif tgt_eth_amount<0:
            rewards=(next_p-now_p)*tgt_eth_amount+(now_p*tgt_eth_amount*fee_ratio)
            ep=now_p
        elif cur_eth_amount>0:
            rewards=-(now_p*cur_eth_amount*fee_ratio)
            ep=0
        elif cur_eth_amount<0:
            rewards=now_p*cur_eth_amount*fee_ratio
            ep=0
    
    if not total_value==0:
        rewardss=rewards*100/total_value
    else :
        rewardss=0
    
    cur_eth_amount=tgt_eth_amount
    cur_eth_value=cur_eth_amount*now_p
    total_value=total_value+rewards
    


train_path='D:/Documents/CODING/Binance_RL_Bot/min_candle/for_train3.db'
con=sqlite3.connect(train_path)
sql='SELECT "O","H","L","C","V","Mean_Price","trade_num","buyer_ratio" FROM eth_1min_kline'
cursor=con.cursor()
cursor.execute(sql)
rows=cursor.fetchall()
con.close()
con=sqlite3.connect('D:/Documents/CODING/Binance_RL_Bot/1st_cost.db')
class Qnet(nn.Module):
    def __init__(self):
        super(Qnet, self).__init__()
        self.fc1 = nn.Linear(2162, 256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
      
    def sample_action(self, obs, epsilon):
        out = self.forward(obs)
        coin = random.random()
        if coin < epsilon:
            return random.randint(0,9)
        else : 
            return out.argmax().item()
            
def train(q, q_target, memory, optimizer):
    global conn
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
        
        sql='INSERT INTO cost ("cost") VALUES (?);'
        print(loss.item())
        con.execute(sql,(float(loss.item()),)) 
        con.commit()       
        


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
q_target = Qnet().to(device)
q_target.load_state_dict(q.state_dict())
memory = ReplayBuffer()
print_interval = 10
optimizer = optim.Adam(q.parameters(), lr=learning_rate)

# for epoch in itertools.count():
for epoch in range(1,120):
    epsilon = max(0.01, 0.1 - 0.01*(epoch/250)) #Linear annealing from 8% to 1%

    current_ratio=0
    total_value=100
    cur_usdt_amount=100
    cur_eth_amount=0
    cur_eth_value=0
    rewardss=0
    ep=0
    now_state=supplyer(0,0,0)
    next_state=0
    isliquidated=False

    for minute in range(1,299340):
        # if minute%1000==0:
        #     print(str(minute)+'/299340')
        #     print(datetime.now())

        now_price=rows[minute+179][3]
        next_price=rows[minute+180][3]
        action=q.sample_action(now_state,epsilon)
        if action<5 and action>0:
            current_ratio=action*(-20)
        elif action>4 and action<9:
            current_ratio=(action-4)*20
        elif action==0:
            current_ratio=0
        elif action==10:
            current_ratio=-1

        if ep>0 and now_price-ep<0 and abs(next_price-ep)*cur_eth_amount/total_value>0.045:     
            isliquidated=True
        elif ep<0 and -ep-now_price<0 and abs(-ep-next_price)*cur_eth_amount/total_value>0.045:
            isliquidated=True
            
        rewarding(current_ratio,now_price,next_price)

        if ep>0 :
            next_state=supplyer(minute,current_ratio,(next_price-ep)*cur_eth_amount/total_value*1000)
        elif ep<0:
            next_state=supplyer(minute,current_ratio,(-ep-next_price)*cur_eth_amount/total_value*1000)
        elif ep==0:
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

    print(str(datetime.now())+'  epoch : '+str(epoch)+' total value : '+str(total_value))
    sensor11=datetime.now()
    if memory.size()>minimum_buffer_size:
        train(q, q_target, memory, optimizer)

    if epoch%print_interval==0 and epoch!=0:
            q_target.load_state_dict(q.state_dict())
            print("Total value : {0}".format(total_value))
            torch.save(q,'D:/Documents/CODING/Binance_RL_Bot/models/model_all_1/{}'.format(str(total_value)+'_'+str(epoch)+'.pt'))
            torch.save(q.state_dict(),'D:/Documents/CODING/Binance_RL_Bot/models/model_save_use_1/{}'.format(str(total_value)+'_'+str(epoch)+'.pt'))
            torch.save(
                {'model_state_dict': q.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),}
                ,'D:/Documents/CODING/Binance_RL_Bot/models/model_checkpoint_1/{}'.format(str(total_value)+'_'+str(epoch)+'.tar')
            )
con.close