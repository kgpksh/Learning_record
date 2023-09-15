def solution(money) :
    global L
    L = len(money)
    return max(dp(money, 1), dp(money, 0))

def dp(money, case):
    dpTable = [0 for _ in range(L)]
    if case :
        dpTable[0] = money[0]
        dpTable[1] = max(money[0], money[1])
    else :
        dpTable[1] = money[1]
        
    for i in range(2, L - case) :
        dpTable[i] = max(dpTable[i - 1], dpTable[i - 2] + money[i])
    
    return max(dpTable)