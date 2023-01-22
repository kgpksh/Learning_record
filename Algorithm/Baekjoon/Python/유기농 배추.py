import sys

def dfs(x,y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    
    if field[y][x] == 1:
        field[y][x] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False
        
def getField(k):
    result = []
    for _ in range(n):
        tmp = []
        for _ in range(m):
            tmp.append(0)
        result.append(tmp)
    
    for _ in range(k):
        x, y = map(int, input().split())
        result[y][x] = 1
        
    return result

sys.setrecursionlimit(2502)            
testCase = int(input())

for _ in range(testCase):
    tmpM,tmpN, k = map(int, input().split())
    global field
    global m
    global n
    m = tmpM
    n = tmpN
    field = getField(k)
    answer = 0
    for w in range(m):
        for h in range(n):
            tmpResult = dfs(w,h)
            if tmpResult:
                answer +=1
    print(answer)