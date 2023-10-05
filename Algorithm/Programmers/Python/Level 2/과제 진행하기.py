from collections import deque
def solution(plans):
    answer = []
    for p in plans :
        p[1] = convertTime(p[1])
        p[2] = int(p[2])
    plans = deque(sorted(plans, key = lambda x : x[1]))
    paused = deque()
    
    currentTask = plans.popleft()
    currentTime = currentTask[1]
    while True :
        if not plans :
            answer.append(currentTask[0])
            while paused :
                answer.append(paused.pop()[0])
            break
            
        plan = plans[0][1]
        currentLeft = currentTask[2]
        diffTime = plan - currentTime
        
        if diffTime < currentLeft :
            currentTask[2] -= diffTime
            paused.append(currentTask)
            currentTask = plans.popleft()
            currentTime = plan
        elif diffTime > currentLeft :
            answer.append(currentTask[0])
            if paused :
                currentTime += currentLeft
                currentTask = paused.pop()
            else :
                currentTime = plan
                currentTask = plans.popleft()
        else :
            answer.append(currentTask[0])
            currentTime += currentLeft
            currentTask = plans.popleft()
        
    return answer

def convertTime(startingTime) :
    H, M = map(int, startingTime.split(":"))
    return 60 * H + M