global n
n = int(input())
scoreBoard = [list(map(int, input().split())) for _ in range(n)]
global answer
answer = 40000

visited = [False] * n

def dfs(depth, index, visited):
    if depth == n//2:
        teamOne = 0
        teamTwo = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    teamOne += scoreBoard[i][j]
                if not visited[i] and not visited[j]:
                    teamTwo += scoreBoard[i][j]
        global answer                
        answer = min(answer, abs(teamOne - teamTwo))

    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1, visited)
            visited[i] = False

dfs(0, 0, visited)    
print(answer)