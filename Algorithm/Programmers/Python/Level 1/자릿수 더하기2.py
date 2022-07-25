from functools import reduce


def solution(n):
    return n if n < 10 else reduce(lambda x, y: int(x) + int(y), str(n))
