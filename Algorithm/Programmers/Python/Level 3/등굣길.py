from collections import deque
def solution(m, n, puddles):
    for puddle in range(len(puddles)) :
        puddles[puddle][0] -= 1
        puddles[puddle][1] -= 1 
        
    grid = [[0 for _ in range(m)] for _ in range(n)]
    grid[0][0] = 1
    
    for X in range(1, m + n - 1) :
        for Y in range(n) :
            y = Y
            x = X - y
            
            if [x, y] in puddles :
                continue
            
            try :
                grid[y][x] += grid[y - 1][x]
            except : pass
        
            try :
                grid[y][x] += grid[y][x - 1]
            except : pass
        
            try :
                grid[y][x] %= 1_000_000_007
            except : pass
            
    return grid[n - 1][m - 1]