from math import sqrt
from math import trunc

def solution(k, d):
    answer = 0
    R = d ** 2
    for x in range(0, d + 1, k) :
        answer += (trunc(sqrt(R - x ** 2)) // k) + 1
    return answer