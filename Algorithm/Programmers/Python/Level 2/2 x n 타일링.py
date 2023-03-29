def solution(n):
    if n == 1 :
        return 1
    if n == 2 :
        return 2
    
    dpTable = [0, 1, 2]
    for i in range(3, n + 1) :
        dpTable.append((dpTable[i - 1] + dpTable[i - 2]) % 1000000007)
    return dpTable[n]