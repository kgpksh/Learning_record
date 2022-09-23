n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

one=[]
two=[0]*n
answer=0
for i,k in enumerate(b):
    one.append([k,i])

one=sorted(one,key= lambda x:x[0])

a.sort(reverse=True)
for i,k in enumerate(one):
    one[i][0]=a[i]

one=sorted(one, key= lambda x:x[1])

for o in range(n):
    answer+=one[o][0]*b[o]

print(answer)