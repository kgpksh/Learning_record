import sys
sys.setrecursionlimit(101000)

n,m,startingPoint = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
global answer
global order
order = 0
answer = {0:0}

for i in range(1, n + 1):
    answer[i] = 0
for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)
    
for i in range(n + 1):
    graph[i] = sorted(graph[i], reverse = True)
    
def dfs(graph, node, visited):
    global answer
    global order
    order +=1
    answer[node] = order
    visited[node] = True
    for g in graph[node]:
        if not visited[g]:
            dfs(graph, g, visited)
                        
dfs(graph, startingPoint, visited)

for result in list(answer.values())[1:]:
    print(result)