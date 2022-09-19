import math
r,c,n=map(int,input().split())
v=math.ceil(r/n)
h=math.ceil(c/n)
print(v*h)