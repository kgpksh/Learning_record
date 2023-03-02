from collections import deque

n, m = map(int, input().split())

field = [list(input()) for _ in range(m)]
horizon = [0, 0, 1, -1]
vertical = [1, -1, 0, 0]

blue = 0
white = 0

for i in range(m) :
    for j in range(n) :
        
        if field[i][j] != 'v' :
            power = 0
            target = field[i][j]
            Q = deque()
            Q.append([i,j])
            field[i][j] = 'v'
            while Q :
                y, x = Q.popleft()
                power += 1
                
                for k in range(4) :
                    nx = x + horizon[k]
                    ny = y + vertical[k]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= m :
                        continue

                    if field[ny][nx] == target :
                        field[ny][nx] = 'v'
                        Q.append([ny, nx])

            if target == 'B' :
                blue += power ** 2

            if target == 'W' :
                white += power ** 2
                
                
print(str(white) + ' ' + str(blue))