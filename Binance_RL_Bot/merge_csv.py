import os
from sqlite3.dbapi2 import Cursor
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
import random   
import time
import csv
import sqlite3

master_df=pd.DataFrame()

# filelist=os.listdir('D:/Documents/CODING/Binance_RL_Bot/aggtrade')
# print('{}'.format(filelist))

path='D:/Documents/CODING/Binance_RL_Bot/aggtrade/'
file_list=os.listdir(path)
file_list_py=[file for file in file_list if file.endswith('.csv')]

con=sqlite3.connect('D:/Documents/CODING/Binance_RL_Bot/pickup/quarter.db')
sql='INSERT INTO alls ("Time","Price","Quantity") VALUES (?,?,?);'

count=1
for i in file_list_py:   
    data=pd.read_csv(path+i,header=None)
    for ro in data.itertuples():
        con.execute(sql,(ro[6],ro[2],ro[3],)) 
        
    count+=1
    if count%20==0 or count>200:
        con.commit()
        print(count)
    count+=1
con.commit()       
con.close
