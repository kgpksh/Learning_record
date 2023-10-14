from math import trunc
from math import ceil
from math import sqrt

def solution(r1, r2):
    answer = 0
    
    mi, ma = min(r1, r2), max(r1, r2)
    r3, r4 = mi ** 2, ma ** 2
    
    for x in range(1, mi + 1) :
        X = x ** 2
        y1 = ceil(sqrt((r3 - X)))
        y2 = trunc(sqrt((r4 - X)))
        answer += y2 - y1 + 1
        
    for x in range(mi + 1, ma + 1) :
        X = x ** 2
        y = trunc(sqrt((r4 - X)))
        answer += y + 1
        
    answer *= 4
    return answer