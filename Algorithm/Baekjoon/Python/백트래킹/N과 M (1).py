from itertools import permutations as p

m, n = map(int, input().split())
l = [i for i in range(1, m + 1)]

for c in p(l, n):
    a = list(map(str, c))
    s = " ".join(a)
    print(s)
