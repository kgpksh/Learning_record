from math import ceil
def solution(n, stations, w):
    answer = 0
    global coverage
    coverage = w
    pos = 1
    for s in stations :
        left = s - coverage
        if pos < left :
            answer += stationsPerEmptySpace(left - pos)
        pos = s + coverage + 1
        
    if pos <= n :
        answer += stationsPerEmptySpace(n + 1 - pos)
    return answer

def stationsPerEmptySpace(width) :
    return ceil(width / (coverage * 2 + 1))