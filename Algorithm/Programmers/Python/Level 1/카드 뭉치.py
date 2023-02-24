from collections import deque

def solution(cards1, cards2, goal):
    one = deque(cards1)
    two = deque(cards2)
    goal = deque(goal)
    
    for i in range(len(goal)) :
        if one and one[0] == goal[i] :
            one.popleft()
            continue
            
        if two and two[0] == goal[i] :
            two.popleft()
            continue
        
        return 'No'
    
    return 'Yes'