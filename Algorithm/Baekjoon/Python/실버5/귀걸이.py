cnt=1
while True:
    n=int(input())
    if n==0:
        break
    name=[]
    check=0
    checklist={}
    for _ in range(n):
        name.append(input())
    for _ in range(2*n-1):
        a,b=map(str,input().split())
        if a in checklist:
            check-=int(a)
        else:
            checklist[a]=True
            check+=int(a)
    print(str(cnt)+' '+name[check-1])
    cnt+=1