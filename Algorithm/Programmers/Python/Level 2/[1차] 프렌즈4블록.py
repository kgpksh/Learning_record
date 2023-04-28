def solution(m, n, board):
    grid = makeMap(m, n ,board)
    answer = 0
    while True :
        record = set()
        
        for y in range(n - 1) :
            for x in range(m - 1) :
                masking(y, x, grid, record)
        record = sorted(record, key = lambda x : (x[0], -x[1]))
        
        if not record :
            break
        answer += len(record)
        fallDown(grid, record)
    return answer

def makeMap(m, n , board) :
    grid = []
    for i in range(n) :
        tmp = []
        for j in range(m) :
            tmp.append(board[j][i])
        grid.append(list(reversed(tmp)))
        
    return grid

def masking(y, x, grid, record) :
    try :
        if grid[y][x] == grid[y + 1][x] == grid[y][x + 1] == grid[y + 1][x + 1] :
            record.add((y, x))
            record.add((y + 1, x))
            record.add((y, x + 1))
            record.add((y + 1, x + 1))
    except : pass
        
def fallDown(grid, coord) :
    for c in coord :
        y, x = c
        del grid[y][x]