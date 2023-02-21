from collections import deque
def solution(numbers):
    length = len(numbers)
    answer = [i for i in range(length)]
    numbers = deque(zip(answer, numbers))
    
    stack = []

    stack.append(numbers.popleft())
    
    while numbers :
        idx, val = numbers[0]
        while True :
            if stack :
                if stack[-1][1] >= val :
                    stack.append(numbers.popleft())
                    break
                tmp = stack.pop()[0]
                answer[tmp] = val
                
            else :
                stack.append(numbers.popleft())
                break
    
    for s in stack :
        idx, val = s
        answer[idx] = -1
    return answer