from collections import Counter


def solution(n):
    answer = 0
    s = str(n)
    lst = sorted(s)
    for i in range(len(lst)):
        answer += int(lst[i]) * 10**i
    return answer
