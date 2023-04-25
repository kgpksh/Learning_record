from collections import deque
def solution(numbers):
    num = deque([(i, n) for i, n in enumerate(numbers)])
    que = deque()
    que.append(num.popleft())
    
    answer = [-1] * len(numbers)
    
    while num :
        while que and num[0][1] > que[-1][1] :
            answer[que[-1][0]] = num[0][1]
            que.pop()
            
        que.append(num.popleft())
        
    return answer