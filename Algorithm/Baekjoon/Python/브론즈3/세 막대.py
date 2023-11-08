import sys

triangle = sorted(list(map(int, sys.stdin.readline().strip().split())))
a, b, c = triangle[0], triangle[1], triangle[2]
print(a + b + min(a + b - 1, c))