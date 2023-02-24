import sys
sys.setrecursionlimit(1000001)
n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [i for i in range(n + 1)]

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

for _ in range(m) :
    c, a, b = map(int, sys.stdin.readline().rstrip().split())
    
    if c == 0 :
        union(parent, a, b)
    else:
        if find(parent, a) == find(parent, b) :
            print('yes')
        else :
            print('no')