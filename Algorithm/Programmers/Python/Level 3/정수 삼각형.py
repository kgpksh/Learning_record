def solution(triangle):
    length = len(triangle)
    for i in range(1, length) :
        for j in range(i + 1) :
            if j == 0 :
                triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                continue
                
            if j == i :
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                continue
                
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
    return max(triangle[-1])