def solution(k, m, score):
    answer = 0
    
    jump = len(score) // m
    score.sort()
    for i in range(1, jump + 1):
        add = score[-1 * i * m] * m
        answer+=add
    return answer