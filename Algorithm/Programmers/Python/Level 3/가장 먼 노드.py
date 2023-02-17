from collections import deque

def solution(n, edge):
    graph = getGraph(n, edge)
    visited = [n + 1] * (n + 1)
    visited[0] = 0
    visited[1] = 0
    
    que = deque([1])
    maximum = 0
    count = 0
    
    while que :
        node = que.popleft()
        distance = visited[node]
        
        for dot in graph[node] :
            if visited[dot] == n + 1 :
                visited[dot] = distance + 1
                que.append(dot)
                
                if distance + 1 == maximum :
                    count += 1
                elif distance + 1 > maximum :
                    maximum = distance + 1
                    count = 1
    return count

def getGraph(n, edge):
    result = [[] for _ in range(n + 1)]
    
    for e in edge:
        a, b = e
        result[a].append(b)
        result[b].append(a)
        
    return result