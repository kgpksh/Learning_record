def solution(numbers, target):
    global answer
    global number
    number = numbers.copy()
    
    answer = 0
    recursive(len(numbers), 0, target)
    
    return answer

def recursive(idx, record, target):
    if idx == 0:
        global answer
        
        if record == target:
            answer += 1
            
    else:
        global number
        recursive(idx-1, record + number[idx - 1], target)
        recursive(idx-1, record - number[idx - 1], target)