# 틀렸음

n=int(input())

a=list(map(int,input().split()))
t=[]
b=[]

for i,k in enumerate(a):
    t.append([i,k])
t=sorted(t,key=lambda x:x[1])

for i,k in enumerate(t):
    t[i].append(i)
    b.append(t[i])

b=sorted(b,key=lambda x:x[0])

answer=[]
for j in b:
    answer.append(str(j[2]))
print(' '.join(answer))