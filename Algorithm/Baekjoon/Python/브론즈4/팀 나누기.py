from itertools import combinations as c
k=list(map(int,input().split()))
s=sum(k)
answer=100000
for i in c(k,2):
    tmp=sum(i)
    answer=min(answer,abs(s-tmp-tmp))
print(answer)