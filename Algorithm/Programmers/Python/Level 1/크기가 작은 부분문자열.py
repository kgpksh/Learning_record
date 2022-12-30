def solution(t, p):
    answer = 0
    stlen = len(t)
    plen = len(p)
    
    for i in range(stlen - plen + 1):
        sliced = int(t[i:i+plen])
        if sliced <= int(p):
            answer+=1
    return answer