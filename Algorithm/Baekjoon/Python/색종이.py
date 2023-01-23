n = int(input())
field = [[False for _ in range(100)] for _ in range(100)]
answer = 0
for _ in range(n):
    X, Y = map(int, input().split())
    
    for y in range(Y, Y + 10):
        for x in range(X, X + 10):
            field[y][x] = True

for y in range(100):
    for x in range(100):
        if field[y][x]:
            answer+=1
print(answer)