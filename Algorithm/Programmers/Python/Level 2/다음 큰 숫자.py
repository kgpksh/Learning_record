def solution(n):
    rec=bin(n)[2:].count('1')
    while True:
        n+=1
        if bin(n)[2:].count('1')==rec:
            break
            
    return n