import sys
from collections import deque
sys.setrecursionlimit(101000)

n,m,startingPoint = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
order = 1
answer = {0:0}

for i in range(1, n + 1):
    answer[i] = 0
for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)
    
for i in range(n + 1):
    graph[i].sort()

d = deque()
d.append(startingPoint)
visited[startingPoint] = True
while d:
    next = d.popleft()
    answer[next] = order
    order+=1
    for g in graph[next]:
        if not visited[g]:
            d.append(g)
            visited[g] = True

for result in list(answer.values())[1:]:
    print(result)