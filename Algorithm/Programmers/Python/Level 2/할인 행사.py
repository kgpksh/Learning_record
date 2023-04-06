from collections import deque
def solution(want, number, discount):
    answer = 0
    wantToBuy = []
    for i in range(len(want)) :
        for j in range(number[i]) :
            wantToBuy.append(want[i])
    wantToBuy.sort()
    
    discountRange = deque(discount[:10])
    
    if wantToBuy == sorted(discountRange) :
        answer += 1
        
    for day in range(10, len(discount)) :
        discountRange.popleft()
        discountRange.append(discount[day])
        
        if wantToBuy == sorted(discountRange) :
            answer += 1
    return answer