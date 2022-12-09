n = int(input())
answer = 1001
for _ in range(n):
    a,b= map(int, input().split())
    
    if a<=b:
        answer = min(answer, b)

if answer == 1001:
    print(-1)
else:
    print(answer)