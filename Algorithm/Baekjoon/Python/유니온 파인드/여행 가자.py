def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]
        
def union(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else :
        parent[a] = b
        
n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]

for i in range(1, n + 1) :
    conn = list(map(int, input().split()))
    for j in range(1, n + 1) :
        if conn[j - 1] == 1 :
            union(parent, i, j)


plan = list(map(int, input().split()))
answer = []

for p in plan :
    answer.append(find(parent, p))

if len(set(answer)) == 1 :
    print('YES')
else :
    print('NO')