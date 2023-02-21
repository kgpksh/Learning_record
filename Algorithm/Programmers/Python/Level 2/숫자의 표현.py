from collections import deque
def solution(n):
    arr = deque()
    answer = 0
    for i in range(1, n+2) :
        while sum(arr) > n :
            arr.popleft()  
            
        if sum(arr) == n :
            answer += 1
            
        arr.append(i)
    return answer