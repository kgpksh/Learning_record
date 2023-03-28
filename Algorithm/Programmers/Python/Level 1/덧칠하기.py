from collections import deque

def solution(n, m, section):
    answer = 1
    cover = section[0] + m - 1
    sec = deque(section)
    
    while sec :
        tmp = sec.popleft()
        if tmp > cover :
            answer += 1
            cover = tmp + m - 1
    
    return answer