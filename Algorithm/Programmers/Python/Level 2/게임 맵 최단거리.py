# BFS는 최단거리를 구하는데 쓰인다. BFS로 처음 간 곳(1인 곳)은 무조건 최단거리이다.

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    upDown = [0, 0, 1, -1]
    leftRight = [1, -1, 0, 0]
    
    que = deque([(0,0)])
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + leftRight[i]
            ny = y + upDown[i]
            
            if nx >= 0 and nx < m and ny >= 0 and ny < n and maps[ny][nx] == 1:
                que.append((nx, ny))
                maps[ny][nx] = maps[y][x] + 1

    if maps[n-1][m-1] == 1: # 도착점에 도달하지 못한 경우
        return -1
    else:
        return maps[n-1][m-1]