from collections import deque
def solution(order):
    idx = 0
    answer = 0
    stk = []
    que = deque([i for i in range(1, len(order) + 1)])
    
    while True :
        stop = True
        while stk and stk[-1] == order[idx] :
            stk.pop()
            idx += 1
            answer += 1
            stop = False
            
        if que :
            if que[0] == order[idx] :
                que.popleft()
                idx += 1
                answer += 1
            else :
                stk.append(que.popleft())
                
            stop = False
        if stop :
            break
        
    return answer