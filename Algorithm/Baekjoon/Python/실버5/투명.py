picture = []
for i in range(100):
    tmp = []
    for j in range(100):
        tmp.append(0)
    picture.append(tmp)

n, m = map(int, input().split())

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    for y in range(y1 - 1, y2):
        for x in range(x1 - 1, x2):
            picture[y][x] = picture[y][x] + 1
            pass
answer = 0
for p in picture:
    for cell in p:
        if cell > m:
            answer +=1

print(answer)