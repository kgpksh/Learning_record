def solution(rows, columns, queries):
    answer = []
    
    point = 1
    matrix = []
    for y in range(rows) :
        tmp = [x for x in range(point, point + columns)]
        point += columns
        matrix.append(tmp)
            
    for q in queries :
        ly, lx, ry, rx = q
        top = [matrix[ly][lx - 1]] + matrix[ly - 1][lx - 1 : rx - 1]
        right = [matrix[y][rx - 1] for y in range(ly - 1, ry - 2)]
        bottom = matrix[ry - 1][lx : rx] + [matrix[ry - 2][rx - 1]]
        left = [matrix[y][lx - 1] for y in range(ly + 1, ry)]
        
        for x in range(lx - 1, rx) :
            matrix[ly - 1][x] = top[x - lx + 1]
        for y in range(ly, ry - 1) :
            matrix[y][rx - 1] = right[y - ly]
        for x in range(lx - 1, rx) :
            matrix[ry - 1][x] = bottom[x - lx + 1]
        for y in range(ly, ry - 1) :
            matrix[y][lx - 1] = left[y - ly]
            
        answer.append(min(top + right + bottom + left))
    return answer