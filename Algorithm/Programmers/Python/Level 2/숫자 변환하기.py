def solution(x, y, n):
    dpTable = [10000001] * (y + 1)
    dpTable[x] = 0
    for i in range(x + 1, y + 1) :
        N = 10000001
        two = 10000001
        three = 10000001
        
        minusN = i - n
        if minusN  >= x :
            N = dpTable[minusN]
            
        divTwo = i // 2
        if i % 2 == 0 and divTwo >= x :
            two = dpTable[divTwo]
        
        divThree = i // 3
        if i % 3 == 0 and divThree >= x :
            three = dpTable[divThree]
        
        result = min(N, two, three)
        if result != 10000001 :
            dpTable[i] = result + 1
            
    if dpTable[y] == 10000001 :
        return -1
    return dpTable[y]