def solution(n, computers):
    answer = 0
    visited = [False] * n
    graph = []
    for c in range(n):
        tmp = []
        for com in range(n):
            if computers[c][com] == 1:
                tmp.append(com)
        graph.append(tmp)
        
    for v in range(n):
        if not visited[v]:
            answer+=1
        dfs(graph, v, visited)   
    return answer

def dfs(graph, n, visited):
    visited [n] = True
    
    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)