n=int(input())

for i in range(1,n+1):
    empty=' '*(2*(n-i))
    star='*'*i
    print(star+empty+star)
for i in range(n-1,0,-1):
    empty=' '*(2*(n-i))
    star='*'*i
    print(star+empty+star)