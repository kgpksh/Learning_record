from collections import deque
def solution(p):
    global converter
    global braketReverser
    converter = {"(" : 1, ")" : -1}
    braketReverser = {"(" : ")", ")" : "("}
    p = deque(p)
    
    return ''.join(recursive(p))
    

def recursive(p) :
    if not p :
        return p
    
    firstBraket = p.popleft()
    isBalance = converter[firstBraket]
    u = deque()
    u.append(firstBraket)
    isCorrect = isBalance >= 0

    while isBalance != 0 :
        braket = p.popleft()
        isBalance += converter[braket]
        isCorrect = isCorrect and isBalance >= 0
        u.append(braket)
        
    result = recursive(p)

    if isCorrect :
        return u + result
    
    answer = deque(['('])
    if result :
        answer += result
    answer.append(')')
    u.popleft()
    u.pop()
    for s in u :
        answer.append(braketReverser[s])
    return answer