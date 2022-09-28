from math import ceil
n,a,b,c,d=map(int,input().split())

A=ceil(n/a)
B=ceil(n/c)

print(min(A*b,B*d))