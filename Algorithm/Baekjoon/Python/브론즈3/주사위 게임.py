tc=int(input())
answer=0
for _ in range(tc):
    a,b,c=map(int,input().split())
    d={}
    d[a]=d.get(a,0)+1
    d[b]=d.get(b,0)+1
    d[c]=d.get(c,0)+1
    dl=sorted(d.items(),key=lambda x:x[0])
    if len(dl)==1:
        answer=max(answer,10000+1000*a)
    elif len(dl)==2:
        for i in range(2):
            if dl[i][1]==2:
                answer=max(answer,1000+dl[i][0]*100)
    else:
        answer=max(answer,dl[2][0]*100)
print(answer)