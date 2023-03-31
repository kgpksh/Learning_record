def solution(n, t, m, p):
    answer = ''
    targetNum = m * (t - 1) + p + 1
    count = 0
    N = -1
    number = []
    
    for i in range(1, targetNum) :
        if not number :
            N += 1
            number = convert(N, n)
            
        tmp = number.pop()
        
        if m == p :
            if i % m == 0 :
                answer += tmp
        else :
            if i % m == p :
                answer += tmp
            
    return answer

def convert(N, t) :
    if N == 0 :
        return ['0']
    result = []
    dict = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    
    while N != 0 :
        tmp = N % t
        
        if tmp > 9 :
            tmp = dict[tmp]
        else :
            tmp = str(tmp)
            
        result.append(tmp)
        N //= t
        
    return result