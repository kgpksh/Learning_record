from collections import deque

tc = int(input())

for _ in range(tc):
    length = int(input())
    visited = [True] * (length + 1)
    answer = 0
    arr = [0] + list(map(int, input().split()))
    
    for i in range(1, length + 1):
        if visited[i]:
            answer +=1
            que = deque([arr[i]])
            visited[i] = False
            while que:
                next = que.popleft()
                if visited[next]:
                    que.append(arr[next])
                    visited[next] = False
                    
    print(answer)