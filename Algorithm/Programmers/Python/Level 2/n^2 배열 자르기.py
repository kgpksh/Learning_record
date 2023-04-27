def solution(n, left, right):
    answer = []
    lefty, leftx = getxy(left, n)
    righty, rightx = getxy(right, n)    
    init = initlist(lefty, n)
    if lefty == righty :
        return init[leftx : rightx + 1]
    answer.extend(init[leftx :])
    for i in range(lefty + 1, righty) :
        for j in range(i) :
            init[j] = i + 1
        answer.extend(init)
        
    
    for i in range(righty) :
        init[i] = righty + 1
    for i in range(rightx + 1) :
        answer.append(init[i])
        
    return answer

def getxy(direction, n) :
    directiony = direction // n
    directionx = direction % n
    
    return directiony, directionx

def initlist(lefty, n) :
    init = [lefty + 1 for _ in range(lefty)]
    nextInit = [i + 1 for i in range(lefty, n)]
    init.extend(nextInit)
    
    return init