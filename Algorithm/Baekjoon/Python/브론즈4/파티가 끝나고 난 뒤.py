a,b=map(int,input().split())
arr=list(map(int,input().split()))
sum=a*b
answer=''
for a in arr:
    answer+=str(a-sum)+' '
print(answer)