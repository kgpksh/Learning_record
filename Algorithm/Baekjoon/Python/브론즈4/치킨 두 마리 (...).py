a,b=map(int,input().split())
p=int(input())

if a+b>=2*p:
    print(a+b-p-p)
else:
    print(a+b)