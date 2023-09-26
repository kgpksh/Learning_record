from collections import Counter
def solution(topping):
    answer = 0
    L = len(set(topping))
    c = Counter(topping)
    
    brother = {}
    brotherTopping = 0
    for t in topping :
        c[t] -= 1
        if c[t] == 0 :
            L -= 1
            
        if not brother.get(t, False) :
            brotherTopping += 1
        
        if brotherTopping == L :
            answer += 1
            
        brother[t] = True
            
        
    return answer