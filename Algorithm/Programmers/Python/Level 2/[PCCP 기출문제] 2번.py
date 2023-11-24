from collections import deque
def solution(land):
    global xMove, yMove, rowLength, colLength, gLand, visited, identifier
    
    xMove, yMove = (1, -1, 0, 0), (0, 0, 1, -1)
    rowLength, colLength = len(land), len(land[0])
    gLand = land
    visited = [[-1 for _ in range(colLength)] for _ in range(rowLength)]
    identifier = 0
    
    for y in range(rowLength) :
        for x in range(colLength) :
            if visited[y][x] == -1 and gLand[y][x] != 0 :
                bfs(y, x)
                identifier += 1
                
    answer = 0
    for x in range(colLength) :
        val = getColValue(x)
        answer = max(answer, val)
    
    return answer

def bfs(y, x) :
    que = deque()
    que.append([y, x])
    visited[y][x] = identifier
    count = 0
    pathRecord = []
    while que :
        y, x = que.popleft()
        pathRecord.append([y, x])
        count += 1
        for move in range(4) :
            nextY = y + yMove[move]
            nextX = x + xMove[move]
            
            if 0 <= nextY < rowLength and 0 <= nextX < colLength :
                if visited[nextY][nextX] == -1 and gLand[nextY][nextX] != 0:
                    visited[nextY][nextX] = identifier
                    que.append([nextY, nextX])
                
    for rec in pathRecord :
        y, x = rec
        gLand[y][x] = count
        
def getColValue(x) :
    result = {}
    for y in range(rowLength) :
        if visited[y][x] == -1 :
            continue
        value = gLand[y][x]
        result[visited[y][x]] = value
    
    return sum(result.values())