def solution(n):
    global m, point, L, keepGoing, answer
    
    m, point, L, keepGoing = n, 1, (n * (1 + n)) // 2, True
    answer = [[0 for i in range(j)] for j in range(1, n + 1)]
    k = 0
    while keepGoing :
        step(k)
        k += 1
    
    return sum(answer, [])

def step(k) :
    global point, keepGoing
    for i in range(2 * k, m - k) :
        answer[i][k] = point
        point += 1
        if point == L + 1 :
            keepGoing = False
            return
    
    for i in range(k + 1, m - (k * 2) - 1) :
        answer[m - k - 1][i] = point
        point += 1
        if point == L + 1:
            keepGoing = False
            return
        
    for i in range(m - k - 1, k * 2, -1) :
        answer[i][i - k] = point
        point += 1
        if point == L + 1 :
            keepGoing = False
            return