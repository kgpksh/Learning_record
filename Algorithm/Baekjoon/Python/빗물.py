height, width = map(int, input().split())
block = list(map(int, input().split()))
world = [[False for _ in range(width)] for _ in range(height)]

for w in range(width) :
    for h in range(height - 1, height - block[w] - 1, -1) :
        world[h][w] = True

answer = 0

for h in range(height) :
    wrapping = False
    tmpCount = 0
    for w in range(width) :
        cell = world[h][w]
        
        if cell :
            answer += tmpCount
            tmpCount = 0
            wrapping = True
        
        else :
            if wrapping :
                tmpCount += 1
            
print(answer)