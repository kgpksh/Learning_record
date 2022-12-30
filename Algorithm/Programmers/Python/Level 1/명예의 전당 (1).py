def solution(k, score):
    answer = []
    
    tmp = []
    
    for s in score:
        
        tmp.append(s)
        t = sorted(tmp, reverse = True)
        
        if len(tmp) < k:
            answer.append(t[-1])
        else:
            answer.append(t[k -1])
    return answer