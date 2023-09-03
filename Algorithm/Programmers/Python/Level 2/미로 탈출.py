from collections import deque

def solution(maps):
    global moveX, moveY, ySize, xSize, maze
    moveX = (1, -1, 0, 0)
    moveY = (0, 0, 1, -1)
    ySize = len(maps)
    xSize = len(maps[0])
    
    maze = [list(row) for row in maps]
    
    start = (0, 0)
    lever = (0, 0)
    for y in range(ySize) :
        for x in range(xSize) :
            if maze[y][x] == 'S' :
                start = (y, x)
                continue
            
            if maze[y][x] == 'L' :
                lever = (y, x)
                continue
                
    toLever = bfs(start[0], start[1], 'L')
    if toLever == -1 :
        return -1
    
    toEscape = bfs(lever[0], lever[1], 'E')
    if toEscape == -1 :
        return -1
    
    return toLever + toEscape

def bfs(y, x, target) :
    que = deque()
    visited = [[0 for _ in range(xSize)] for _ in range(ySize)]
    que.append((y, x))
    
    while que :
        y, x = que.popleft()
        if maze[y][x] == target :
            return visited[y][x]
        
        for move in range(4) :
            nextY = y + moveY[move]
            nextX = x + moveX[move]
            
            if 0 <= nextY < ySize and 0 <= nextX < xSize and visited[nextY][nextX] == 0 and maze[nextY][nextX] != 'X':
                que.append((nextY, nextX))
                visited[nextY][nextX] = visited[y][x] + 1
                
    return -1