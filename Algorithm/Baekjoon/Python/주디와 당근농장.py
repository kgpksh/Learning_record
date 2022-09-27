from collections import deque as d
n,r,c=map(int,input().split())
sample=d()
sample2=d()
if c%2==0:
    sample=d()
    for i in range(n):
        if i%2==0:
            sample.append('.')
            sample2.append('v')
            
        else:
            sample.append('v')
            sample2.append('.')
else:
    sample=d()
    for i in range(n):
        if i%2!=0:
            sample.append('.')
            sample2.append('v')
        else:
            sample.append('v')
            sample2.append('.')

check=r%2


for i in range(1,n+1):
    if i%2==check:
        print(''.join(sample))
    else:
        print(''.join(sample2))