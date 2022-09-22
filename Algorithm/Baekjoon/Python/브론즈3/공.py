n=int(input())
L=[0,1,2,3]
for _ in range(n):
    a,b=map(int,input().split())
    i1=L.index(a)
    i2=L.index(b)
    L[i1]=b
    L[i2]=a
print(L[1])