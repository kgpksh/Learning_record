n=int(input())

for i in range(n,0,-1):
    empty=' '*(n-i)
    star='*'*(2*i-1)
    print(empty+star)

for i in range(2,n+1):
    empty=' '*(n-i)
    star='*'*(2*i-1)
    print(empty+star)