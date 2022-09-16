a=[]
b=[]
n,m=map(int,input().split())
for _ in range(n):
    a.append(list(map(int,input().split())))
for _ in range(n):
    b.append(list(map(int,input().split())))

for i in range(n):
    tmp=""
    for j in range(m):
        if j==m-1:
            tmp+=str(a[i][j]+b[i][j])+""
        else:
            tmp+=str(a[i][j]+b[i][j])+" "
    print(tmp)