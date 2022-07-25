from collections import Counter


def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    answer = 1
    for d in dic.values():
        answer *= d + 1
    return answer - 1
