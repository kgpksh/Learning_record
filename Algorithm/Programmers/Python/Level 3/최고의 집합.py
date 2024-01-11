def solution(n, s):
    if s < n :
        return [-1]
    
    div = s // n
    answer = [div] * n
    for i in range(1, s - div * n + 1) :
        answer[-i] += 1
    return answer