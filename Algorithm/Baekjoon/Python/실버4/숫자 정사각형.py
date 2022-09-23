n,m=map(int,input().split())
L=[]
for _ in range(n):
    L.append(input())

answer=1
for i in range(1,min(n,m)):
    for j in range(n-i):
        for h in range(m-i):
            lt=int(L[j][h])
            rt=int(L[j][h+i])
            ld=int(L[j+i][h])
            rd=int(L[j+i][h+i])

            if lt==rt==ld==rd:
                answer=max(answer,(i+1)**2)
print(answer)