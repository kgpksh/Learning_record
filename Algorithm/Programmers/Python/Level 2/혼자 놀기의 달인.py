def solution(cards):
    L = len(cards)
    
    global visited
    global cardList
    cardList = cards
    visited = [False] * L
    
    answer = [0]
    
    for l in range(L) :
        if not visited[l] :
            answer.append(recursive(l, 0))
            
    answer.sort()
    
    return answer[-1] * answer[-2]
    
def recursive(index, score) :
    if visited[index] :
        return score
    
    visited[index] = True
    card = cardList[index]
    score += 1
    return recursive(card - 1, score)