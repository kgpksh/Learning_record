from collections import deque

node = int(input())
line = int(input())
visited = [False] * (node + 1)
graph = [[] for _ in range(node + 1)]
answer = 0
for _ in range(line):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)
    
que = deque([1])
visited[1] = True

while que:
    next = que.popleft()
    for computer in graph[next]:
        if not visited[computer]:
            visited[computer] = True
            que.append(computer)
            answer += 1
            
print(answer)