def solution(s, skip, index):
    answer = []
    for char in s :
        code = ord(char)
        count = index
        while count > 0 :
            if code == ord('z') :
                code = ord('a')
            else :
                code += 1
            
            if chr(code) not in skip :
                count -= 1
        
        answer.append(chr(code))
        
    return ''.join(answer)