def solution(board):
    Ysize = len(board)
    Xsize = len(board[0])
    
    if Ysize == 1 and Xsize == 1 :
        return board[0][0]
    
    answer = 0
    for y in range(1, Ysize) :
        for x in range(1, Xsize) :
            up = board[y - 1][x]
            left = board[y][x - 1]
            upperLeft = board[y - 1][x - 1]
            
            if board[y][x] != 0 :
                board[y][x] = min(upperLeft, up, left) + 1
                answer = max(answer, board[y][x])
                
    return answer * answer