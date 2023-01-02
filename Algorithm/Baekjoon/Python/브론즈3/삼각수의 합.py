def g(n):
    return ((1 + n) * n) // 2
    
tc = int(input())

for _ in range(tc):
    n = int(input())
    answer = 0
    
    for i in range(1,n+1):
        answer += i * g(i + 1)
        
    print(answer)