def thousand(x, y):
    return x * 1000 / y

a, b= map(int, input().split())
answer = thousand(a,b)

tc = int(input())

for _ in range(tc):
    a, b= map(int, input().split())
    answer = min(answer, thousand(a,b))
    
print(answer)