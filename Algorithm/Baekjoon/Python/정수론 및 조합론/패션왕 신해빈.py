n = int(input())
for i in range(n):
    d = {}
    m = int(input())
    for j in range(m):
        a, b = map(str, input().split())
        d[b] = d.get(b, 0) + 1
    answer = 1
    for k in d.values():
        answer *= k + 1
    print(answer - 1)
