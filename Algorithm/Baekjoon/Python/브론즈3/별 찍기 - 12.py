n=int(input())
for i in range(1,n+1):
    empty=' '*(n-i)
    print(empty+'*'*i)
for i in range(n-1,0,-1):
    empty=' '*(n-i)
    print(empty+'*'*i)