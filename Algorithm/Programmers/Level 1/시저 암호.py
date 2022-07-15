def solution(s, n):
    answer = ''
    for i in s:
        if i.islower():
            answer+=push(i,'z',n)
        elif i.isupper():
            answer+=push(i,'Z',n)
        elif i==' ':
            answer+=' '
    
    return answer

def push(c,z,d):
    if ord(c)+d>ord(z):
        return chr(ord(c)+d-26)
    else:
        return chr(ord(c)+d)