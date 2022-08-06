import sys

n = int(input())
l = list(map(int, sys.stdin.readline().rstrip().split()))
l.sort()
print(l[0] * l[-1])
