from math import sqrt
from math import ceil
def solution(begin, end):
    answer = []
    if begin == 1 :
        answer.append(0)
        begin += 1
        
    for i in range(begin, end + 1) :
        candidates = [1]
        
        for div in range(2, ceil(sqrt(i)) + 1) :
            if i % div == 0 :
                if div != i :
                    candidates.append(div)
                    
                tmp = i // div
                if tmp <= 10000000 and tmp != i:
                    candidates.append(tmp)
                    
        answer.append(max(candidates))
                    
    return answer