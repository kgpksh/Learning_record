tc=int(input())
for _ in range(tc):
    a,b=map(int,input().split())
    print((a//2)*b+((a%2)*b)//2)