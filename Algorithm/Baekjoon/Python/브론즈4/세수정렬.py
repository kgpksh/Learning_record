arr=list(map(int,input().split()))
arr.sort()
answer=''
for a in arr:
    answer+=str(a)+' '
print(answer)