graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

dfs_visited = [False] * len(graph)
bfs_visited = [False] * len(graph)

def dfs(graph, n, visited):
    visited[n] = True

    print(n, end=" ")

    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, dfs_visited)