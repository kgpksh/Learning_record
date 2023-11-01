board = []
for _ in range(5) :
    board.append(input())

answer = []
for x in range(15) :
    for y in range(5) :
        try :
            answer.append(board[y][x])
        except :
            pass
print(''.join(answer))