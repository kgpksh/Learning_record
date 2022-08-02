import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
a = set(sys.stdin.readline().rstrip().split())
b = set(sys.stdin.readline().rstrip().split())
print(len(a - b) + len(b - a))
