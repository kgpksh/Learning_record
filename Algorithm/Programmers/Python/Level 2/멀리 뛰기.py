def solution(n):
    if n == 1:
        return 1
    
    dpTable = [0] * (n + 1)
    dpTable[1] = 1
    dpTable[2] = 2
    
    for i in range(3, n + 1) :
        dpTable[i] = (dpTable[i - 2] + dpTable[i - 1]) % 1234567
    
    return dpTable[n]