from math import lcm
import sys

n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(lcm(a, b))
