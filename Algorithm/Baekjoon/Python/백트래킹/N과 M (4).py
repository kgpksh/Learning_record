from itertools import combinations_with_replacement as c

m, n = map(int, input().split())
l = [i for i in range(1, m + 1)]

for c in c(l, n):
    a = list(map(str, c))
    s = " ".join(a)
    print(s)
