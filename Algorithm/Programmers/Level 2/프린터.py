from collections import deque


def solution(p, l):
    answer = 0
    while True:
        m = max(p)
        get = p.pop(0)
        if m == get:
            answer += 1
            if l == 0:
                break
            else:
                l -= 1
        else:
            p.append(get)
            if l == 0:
                l = len(p) - 1
            else:
                l -= 1
    return answer
