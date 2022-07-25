from itertools import combinations


def solution(nums):
    c = list(combinations(nums, 3))
    answer = len(list(c))
    for i in c:
        s = sum(i)
        for j in range(2, s):
            if s % j == 0:
                answer -= 1
                break
    return answer
