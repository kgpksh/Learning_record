from math import factorial as f
tc=int(input())

for _ in range(tc):
    n,m=map(int,input().split())
    print(int((f(m) / ( f(n) * f(m-n) ) )))