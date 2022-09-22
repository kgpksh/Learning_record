while True:
    branch=list(map(int,input().split()))
    if branch[0]==0:
        break
    answer=1
    for i in range(1,(branch[0]*2)+1):
        if i%2==1:
            answer*=branch[i]
        else:
            answer-=branch[i]
    print(answer)