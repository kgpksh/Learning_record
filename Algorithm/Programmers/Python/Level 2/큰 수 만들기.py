from collections import deque
def solution(number, k):
    number = deque(number)
    stk = []
    cnt = 0
    
    while cnt < k and number:
        while stk and number[0] > stk[-1] :
            stk.pop()
            cnt += 1
            if cnt == k :
                break
        stk.append(number.popleft())
    if cnt < k :
        return ''.join(stk[: -1]) + ''.join(number)
    return ''.join(stk) + ''.join(number)