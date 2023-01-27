n = int(input())
field = [input() for _ in range(n)]
visited = []
for f in field:
    tmp = []
    for r in f:
        if r=='1':
            tmp.append(False)
        else:
            tmp.append(True)
    visited.append(tmp)
          
def dfs(visited, x, y, n):
    if x < 0 or x >=n or y < 0 or y >= n:
        return False
    if visited[y][x]:
        return False
    
    global count
    count += 1
    visited[y][x] = True
    dfs(visited, x + 1, y, n)
    dfs(visited, x - 1, y, n)
    dfs(visited, x, y + 1, n)
    dfs(visited, x, y - 1, n)
    return True

answer = 0
numbers = []
for row in range(n):
    for col in range(n):
        global count
        count = 0
        if dfs(visited, row, col, n):
            answer+=1
        if count > 0:
            numbers.append(count)
        count = 0
print(answer)
numbers.sort()
for n in numbers:
    print(n)
