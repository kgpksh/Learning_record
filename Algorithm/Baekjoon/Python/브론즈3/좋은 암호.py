a,b=map(int,input().split())
check=True
for i in range(2,b):
    if a%i==0:
        print('BAD '+str(min(a//i,i)))
        check=False
        break
if check:
    print('GOOD')