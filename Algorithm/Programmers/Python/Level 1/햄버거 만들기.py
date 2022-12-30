def solution(ingredient):
    answer = 0
    stk = []
    
    for i in ingredient:
        stk.append(i)
        tmp = stk[-4:-1]
        tmp.append(stk[-1])
        
        if tmp == [1,2,3,1]:
            answer+=1
            stk.pop()
            stk.pop()
            stk.pop()
            stk.pop()
            
    return answer