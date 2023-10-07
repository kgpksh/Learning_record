from collections import deque
def solution(que1, que2):
    que1 = deque(que1)
    que2 = deque(que2)
    answer = 0
    s1 = sum(que1)
    s2 = sum(que2)
    
    if (s1 + s2) % 2 == 1 :
        return -1
    
    cnt = (len(que1) + len(que2)) * 4
    while que1 and que2 and cnt != 0:
        if s1 == s2 :
            return answer
        
        if s1 < s2 :
            tmp = que2.popleft()
            que1.append(tmp)
            s1 += tmp
            s2 -= tmp
        else :
            tmp = que1.popleft()
            que2.append(tmp)
            s1 -= tmp
            s2 += tmp
        
        answer += 1
        cnt -= 1
        
    return -1