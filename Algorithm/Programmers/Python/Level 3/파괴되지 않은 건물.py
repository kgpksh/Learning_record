def solution(board, skill):
    skillType = {1 : -1, 2 : 1}
    bcLength = len(board)
    brLength = len(board[0])
    tmpRec = [[0] * (brLength + 1) for _ in range(bcLength + 1)]
    
    for ty, r1, c1, r2, c2, degree in skill :
        tmpRec[r1][c1] += degree * skillType[ty]
        tmpRec[r2 + 1][c1] -= degree * skillType[ty]
        tmpRec[r1][c2 + 1] -= degree * skillType[ty]
        tmpRec[r2 + 1][c2 + 1] += degree * skillType[ty]
        
    for y in range(bcLength + 1) :
        for x in range(brLength) :
            tmpRec[y][x + 1] += tmpRec[y][x]
            
    for x in range(brLength + 1) :
        for y in range(bcLength) :
            tmpRec[y + 1][x] += tmpRec[y][x]
            
    answer = 0
    for y in range(bcLength) :
        for x in range(brLength) :
            board[y][x] += tmpRec[y][x]
            if board[y][x] > 0 :
                answer += 1
    return answer