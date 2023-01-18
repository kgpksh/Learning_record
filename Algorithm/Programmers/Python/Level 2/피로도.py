from itertools import permutations as p

def solution(k, dungeons):
    answer = -1
    for d in list(p(dungeons, len(dungeons))):
        answer = max(answer, iteration(k,d))
    return answer

def iteration(k, order):
    result = 0
    for o in order:
        if k >= o[0]:
            result +=1
            k-= o[1]
    return result