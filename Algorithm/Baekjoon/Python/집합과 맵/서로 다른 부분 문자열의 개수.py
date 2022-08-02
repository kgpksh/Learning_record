import sys

st = sys.stdin.readline().rstrip()

s = set()

l = len(st)
for i in range(1, l + 1):
    for j in range(l - i + 1):
        s.add(st[j : j + i])
print(len(s))
