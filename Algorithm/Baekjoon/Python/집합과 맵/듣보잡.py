import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
heard = set()
seen = set()

for h in range(m):
    heard.add(sys.stdin.readline().rstrip())
for s in range(n):
    seen.add(sys.stdin.readline().rstrip())

hs = sorted(heard & seen)
print(len(hs))
for a in hs:
    print(a)
