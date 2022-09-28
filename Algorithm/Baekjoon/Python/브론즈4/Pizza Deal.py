from math import pi
a,p1=map(int,input().split())
r,p2=map(int,input().split())

circle=((r**2)*pi)/p2
slice=a/p1

if circle>slice:
    print('Whole pizza')
else:
    print('Slice of pizza')