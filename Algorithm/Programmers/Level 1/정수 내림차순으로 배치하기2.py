def solution(n):
    s = sorted(str(n), reverse=True)
    return int("".join(s))
