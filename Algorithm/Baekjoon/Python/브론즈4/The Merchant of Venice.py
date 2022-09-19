import math
tc=int(input())
for i in range(1,tc+1):
    result='Data Set {0}:\n'.format(i)
    n,s,d=map(int,input().split())
    answer=0
    for _ in range(n):
        dt,v=map(int,input().split())
        if math.ceil(dt/s)<=d:
            answer+=v
    result+=str(answer)
    print(result)
    if i!=tc:
        print('')