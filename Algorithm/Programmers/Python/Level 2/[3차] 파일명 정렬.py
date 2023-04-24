from collections import deque
def solution(files):
    sliced = []
    answer = []
    for file in files :
        sliced.append(sliceString(file))
    
    sliced = sorted(sliced, key = lambda x : (x[0], x[1]))
    
    for name in sliced :
        _, num, tail, head, zeros = name
        
        num = num[zeros :]
        answer.append(head + num + tail)
    return answer

def sliceString(fileName) :
    head = []
    number = deque()
    tail = ''
    result = []
    fileName = deque(fileName)
    
    isNumber = False
    while fileName :
        name = fileName[0]
        if not isNumber and not name.isdigit() :
            head.append(name)
            fileName.popleft()
            continue
        
        if name.isdigit() :
            isNumber = True
            number.append(name)
            fileName.popleft()
            continue
            
        if isNumber and not name.isdigit() :
            tail = ''.join(fileName)
            break
    
    zeros = 5 - len(number)
    for i in range(zeros) :
        number.appendleft('0')
    
    headString = ''.join(head)
    numString = ''.join(number)
    
    result.append(headString.lower())
    result.append(numString)
    result.append(tail)
    result.append(headString)
    result.append(zeros)
    return result