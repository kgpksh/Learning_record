a,b=map(int,input().split())

if a%4==0:
    h1=a//4-1
    v1=4
else:
    h1=a//4
    v1=a%4

if b%4==0:
    h2=b//4-1
    v2=4
else:
    h2=b//4
    v2=b%4
print(abs(h2-h1)+abs(v2-v1))