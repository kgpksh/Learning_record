a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

if b%d==0:
    math=b//d
else:
    math=(b//d)+1

if c%e==0:
    korean=c//e
else:
    korean=(c//e)+1    
print(a-max(math,korean))