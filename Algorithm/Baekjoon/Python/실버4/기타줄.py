from math import ceil as c
n,m=map(int,input().split())
six=1001
one=1001
for i in range(m):
    a,b=map(int,input().split())
    six=min(six,a)
    one=min(one,b)
    
if six>one*6:
    print(n*one)
elif c(n/6)*six<=(n//6)*six+(n%6)*one:
    print(c(n/6)*six)
else:
    print((n//6)*six+(n%6)*one)