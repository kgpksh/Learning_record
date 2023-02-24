def solution(keymap, targets):
    answer = []
    for target in targets :
        count = 0
        
        for char in target :
            press = find(keymap, char)
            if press == 101 :
                count = -1
                break
            else :
                count += press + 1
        
        answer.append(count)
    return answer

def find(keymap, target) :
    index = 101
    for k in keymap :
        try :
            index = min(index, k.index(target))
        except :
            pass
    return index