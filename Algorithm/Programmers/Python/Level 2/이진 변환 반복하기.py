def solution(s):
    if s=='1':
        return [0,0]
    
    change=0
    zeros=0
    while True:
        zeros+=s.count('0')
        change+=1
        s=bin(len(s.replace('0','')))[2:]
        if s=='1':
            break
    return [change,zeros]