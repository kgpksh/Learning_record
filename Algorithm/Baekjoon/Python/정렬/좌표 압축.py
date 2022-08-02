import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split()))
s = sorted(set(l))
d = {}

for i, v in enumerate(s):
    d[v] = i

print = sys.stdout.write
for i in l:
    print(f"{d[i]} ")
