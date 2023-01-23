from collections import deque
node, edge, startingPoint = map(int, input().split())

graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    start, destination = map(int, input().split())
    if not start in graph[destination]:
        graph[destination].append(start)
        graph[destination].sort()
    if not destination in graph[start]:
        graph[start].append(destination)
        graph[start].sort()
        
dfsVisited = [False] * (node + 1)
bfsVisited = [False] * (node + 1)

global dfsAnswer
global bfsAnswer
dfsAnswer = []
bfsAnswer = []

def dfs(graph, v, visited):
    visited[v] = True
    global dfsAnswer
    dfsAnswer.append(str(v))
    for g in graph[v]:
        if not visited[g]:
            dfs(graph, g, visited)
            
def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True
    global bfsAnswer
    bfsAnswer.append(str(start))
    while que:
        v = que.popleft()
        for g in graph[v]:
            if not visited[g]:
                visited[g] = True
                que.append(g)
                bfsAnswer.append(str(g))

dfs(graph, startingPoint, dfsVisited)
bfs(graph, startingPoint, bfsVisited)

print(' '.join(dfsAnswer))
print(' '.join(bfsAnswer))