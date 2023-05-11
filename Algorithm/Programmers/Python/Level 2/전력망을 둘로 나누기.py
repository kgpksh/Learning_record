from collections import deque
def solution(n, wires):
    answer = n
    graph = makeGraph(n, wires)
    
    for v1, v2 in wires :
        graph[v1][v2] = True
        graph[v2][v1] = True
        
        count = bfsCount(n, v1, graph)
        diff = abs(n - count - count)
        answer = min(answer, diff)
        
        graph[v1][v2] = False
        graph[v2][v1] = False
    return answer

def makeGraph(n, wires) :
    result = [[True for _ in range(n + 1)] for _ in range(n + 1)]
    for v1, v2 in wires :
        result[v1][v2] = False
        result[v2][v1] = False
        
    return result
def copyGraph(graph) :
    result = []
    for g in graph :
        row = []
        for element in g :
            row.append(element)
        result.append(row)
    return result

def bfsCount(n, v1, graph) :
    tmpGraph = copyGraph(graph)
    que = deque([v1])
    count = 1
    while que :
        start = que.popleft()
        for node in range(1, n + 1) :
            if not tmpGraph[start][node] :
                tmpGraph[start][node] = True
                tmpGraph[node][start] = True
                que.append(node)
                count += 1
    return count