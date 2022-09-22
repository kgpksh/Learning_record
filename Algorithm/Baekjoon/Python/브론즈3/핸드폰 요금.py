import math
n=int(input())
L=list(map(int,input().split()))

y=0
m=0
for l in L:
    y+=math.ceil(l/30)*10
    if l%30==0:
        y+=10
    m+=math.ceil(l/60)*15
    if l%60==0:
        m+=15
if y>m:
    print('M '+str(m))
elif y<m:
    print('Y '+str(y))
else:
    print('Y M '+str(y))