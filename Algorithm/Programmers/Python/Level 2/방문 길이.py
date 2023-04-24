def solution(dirs):
    answer = 0
    control = {'L' : (-1, 0), 'R' : (1, 0), 'U' : (0, 1), 'D' : (0, -1)}
    x, y = 0, 0
    record = set()
    for d in dirs :
        dx, dy = control[d]
        dx += x
        dy += y
        if dx < -5 or dx > 5 or dy < -5 or dy > 5 :
            continue
        X = tuple(sorted([x, dx]))
        Y = tuple(sorted([y, dy]))
        
        x = dx
        y = dy
        
        record.add((X,Y))
        
    for r in record :
        x, y = r
        answer += x[1] - x[0]
        answer += y[1] - y[0]
    return answer