from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        dic = {}
        for j in orders:
            for l in combinations(sorted(j), c):
                dic[l] = dic.get(l, 0) + 1
        d = sorted(list(dic.items()), key=lambda x: -x[1])
        n = 2
        for b in d:
            if b[1] >= n:
                n = b[1]
                answer.append("".join(b[0]))
    answer.sort()
    return answer
