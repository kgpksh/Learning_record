from collections import deque
def solution(s):
    answer = 0
    d = deque(s)
    
    x = d[0]
    
    standard = 0
    others = 0
    
    for i in range(len(s)):
        p = d.popleft()
        if p == x:
            standard+=1
        else:
            others+=1
        
        if len(d) == 0:
            answer +=1
            break
        
        if standard == others:
            x = d[0]
            standard = 0
            others = 0
            answer +=1
    return answer