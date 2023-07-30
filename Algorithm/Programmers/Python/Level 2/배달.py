from collections import deque
def solution(N, road, K):
    road = makeMap(road)
    visited = [float('inf')] * (N + 1)
    visited[1] = 0
    
    answer = 0
    que = deque()
    que.append(1)
    
    while que :
        start = que.popleft()
        
        for town, distance in road[start].items() :
            offer = visited[start] + distance
            if offer < visited[town] :
                que.append(town)
                visited[town] = offer
    
    for v in visited :
        if v <= K :
            answer += 1
    return answer

def makeMap(road) :
    result = {}
    for a, b, l in road :
        tmpA = result.get(a, {})
        tmpA[b] = min(l, tmpA.get(b, 10001))
        
        tmpB = result.get(b, {})
        tmpB[a] = min(l, tmpB.get(a, 10001))
        
        result[a] = tmpA
        result[b] = tmpB
    
    return result