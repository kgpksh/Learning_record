import sys
from collections import deque

global N, moveY, moveX

N = int(sys.stdin.readline().rstrip())
moveY = (0, 0, 1, -1)
moveX = (1, -1, 0, 0)

def makeMap() :
    result = []
    for _ in range(N) :
        result.append(list(map(int, sys.stdin.readline().rstrip())))
    
    return result

def searchSingleBlockByBfs(y, x) :
    que = deque()
    result = 1
    que.append((y, x))
    squareMap[y][x] = 0

    while que :
        y, x = que.popleft()

        for step in range(4) :
            movedY = y + moveY[step]
            movedX = x + moveX[step]

            if 0 <= movedY < N and 0 <= movedX < N and squareMap[movedY][movedX] == 1 :
                que.append((movedY, movedX))
                squareMap[movedY][movedX] = 0
                result += 1
    
    return result


global squareMap
squareMap = makeMap()

count = 0
blockSizes = []
for y in range(N) :
    for x in range(N) :
        if squareMap[y][x] == 1 :
            count += 1
            blockSizes.append(searchSingleBlockByBfs(y, x))

print(count)

blockSizes.sort()

for blockSize in blockSizes :
    print(blockSize)