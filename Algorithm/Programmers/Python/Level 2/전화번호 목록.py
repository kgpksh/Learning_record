def solution(p):
    answer = True

    p.sort()

    for a, b in zip(p, p[1:]):
        if b.startswith(a):
            return False

    return answer
