def solution(name):
    length = len(name)
    if length == 1 :
        return changeAlpha(name)
    
    start = 0
    
    for l in range(length - 1, -1, -1):
        tmp = 'A' * l
        try :
            start = name[1 : ].index(tmp)
            break
        except :
            pass
        
    back = length - start - l - 1
    answer = max(start, back) + min(start, back) * 2
    
    
    straight = []
    for i, c in enumerate(name) :
        if c != 'A' :
            straight.append(i)
    if straight :
        answer = min(answer, straight[-1], length - straight[0])
    
    
    for n in name :
        answer += changeAlpha(n)
    return answer

def changeAlpha(c) :
    return min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)