def solution(places):
    answer = []
    for p in places :
        answer.append(validate(p))
        
    return answer

def validate(room) :
    move = [(0, -2), (0, 2), (-2, 0), (2, 0), (-1, -1), (-1, 1), (1, 1)
            , (1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

    for row in range(5) :
        for col in range(5) :
            here = room[row][col]
            
            if here != 'P' :
                continue

            for X, Y in move :
                x = col + X
                y = row + Y
                
                if x < 0 or x > 4 or y < 0 or y > 4 :
                    continue
                
                target = room[y][x]
                
                if target != 'P' :
                    continue

                if (abs(X) == 1 and abs(Y) == 0) or (abs(X) == 0 and abs(Y) == 1) :
                    return 0


                if abs(X) == 1 and abs(Y) == 1:
                    one = room[row][x]
                    two = room[y][col]

                    if one != 'X' or two != 'X' :
                        return 0
                    continue

                if abs(X) == 2 :
                    tmpX = (col + x) // 2
                    if room[row][tmpX] != 'X' :
                        return 0
                    continue

                if abs(Y) == 2 :
                    tmpY = (row + y) // 2
                    if room[tmpY][col] != 'X' :
                        return 0
    return 1