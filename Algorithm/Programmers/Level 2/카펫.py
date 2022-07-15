import math


def solution(brown, yellow):
    root = math.trunc(yellow ** (1 / 2))
    yaksu = []
    for i in range(1, root + 1):
        if yellow % i == 0:
            yaksu.append(yellow / i)
    yaksu.sort()
    for i in yaksu:
        if (i + 2) * ((yellow / i) + 2) == brown + yellow:
            return [i + 2, ((yellow / i) + 2)]
