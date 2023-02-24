from collections import Counter

def solution(k, tangerine):
    answer = 0
    tan = sorted(Counter(tangerine).items(), key = lambda x : -x[1])
    
    count = 0
    for i in range(len(tan)) :
        answer += 1
        
        if count + tan[i][1] >= k :
            break
            
        count += tan[i][1]
    return answer