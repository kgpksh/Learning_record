n=int(input())
for i in range(n,0,-1):
    empty=' '*(((2*n-1)-(2*i-1))//2)
    s=empty+'*'*(2*i-1)
    print(s)