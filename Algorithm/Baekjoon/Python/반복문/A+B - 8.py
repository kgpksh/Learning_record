import sys

t = int(input())

for i in range(t):
    m, n = map(int, sys.stdin.readline().rstrip().split())
    print("Case #{0}: {1} + {2} = {3}".format(i + 1, m, n, m + n))
