from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst2 = combinations(lst, 3)

best = 0
for i in lst2:
    s = sum(i)
    if s <= m and s > best:
        best = s
print(best)
