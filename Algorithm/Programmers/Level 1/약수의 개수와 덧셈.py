import math


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        sqrt = math.trunc(i ** (1 / 2))
        if sqrt**2 == i:
            answer -= i
        else:
            answer += i

    return answer
