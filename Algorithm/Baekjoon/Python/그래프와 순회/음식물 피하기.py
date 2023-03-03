from collections import deque

n, m, k = map(int, input().split())

rectangle = [[False] * (m + 1) for _ in range((n + 1))]

for _ in range(k) :
    r, c = map(int, input().split())
    rectangle[r][c] = True

horizon = [0, 0, 1, -1]
vertical = [1, -1, 0, 0]
answer = 0

for i in range(1, n + 1) :
    for j in range(1, m + 1) :
        if rectangle[i][j] :
            size = 1
            Q = deque()
            Q.append((i, j))
            rectangle[i][j] = False
            
            while Q :
                y, x = Q.popleft()
                
                for g in range(4) :
                    ny = y + vertical[g]
                    nx = x + horizon[g]
                    
                    if ny < 1 or ny > n or nx < 1 or nx > m :
                        continue
                        
                    if rectangle[ny][nx] :
                        size += 1
                        Q.append((ny, nx))
                        rectangle[ny][nx] = False
                        
            answer = max(answer, size)
            
print(answer)