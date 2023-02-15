def solution(numbers):
    if len(set(numbers)) == 1 and numbers[0] == 0:
        return '0'
    strings = []
    for n in numbers:
        strings.append(str(n) * 4)
        
    strings.sort(reverse = True)
    
    answer = []
    for s in strings:
        answer.append(s[:len(s)//4])
    
    return ''.join(answer)