def solution(babbling):
    available = ["aya", "ye", "woo", "ma"]
    
    answer = 0
    
    for b in babbling :
        okay = True
        startLength = len(b)
        
        for a in available :            
            if len(b.replace(a*2, a)) != startLength :
                okay = False
                break
        
        allowed = 0
        for a in available :
            allowed += b.count(a) * len(a)
        
        if startLength != allowed :
            okay = False
            
        if okay :
            answer +=1
    return answer