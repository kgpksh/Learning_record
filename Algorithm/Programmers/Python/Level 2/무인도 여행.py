from collections import deque

def solution(maps):
    answer = []
    maps = toList(maps)
    maxY = len(maps)
    maxX = len(maps[0])
    
    for y in range(maxY) :
        for x in range(maxX) :
            if maps[y][x] != 'X' :
                answer.append(bfs(maps, y, x, maxY, maxX))
                
    if not answer :
        return [-1]
    
    return sorted(answer)

def toList(maps) :
    result = []
    for string in maps :
        result.append(list(string))
    
    return result

def bfs(maps, Y, X, maxY, maxX) :
    moveX = [-1, 1, 0, 0]
    moveY = [0, 0, 1, -1]
    result = 0
    
    que = deque()
    que.append((Y, X))
    result += int(maps[Y][X])
    maps[Y][X] = 'X'
    
    while que :
        y, x = que.popleft()
        for i in range(4) :
            tmpY = y + moveY[i]
            tmpX = x + moveX[i]
            if tmpY < 0 or tmpY >= maxY or tmpX < 0 or tmpX >= maxX or maps[tmpY][tmpX] == 'X' :
                continue
            
            que.append((tmpY, tmpX))
            result += int(maps[tmpY][tmpX])
            maps[tmpY][tmpX] = 'X'
    return result