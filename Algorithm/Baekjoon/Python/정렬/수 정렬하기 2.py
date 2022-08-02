import sys

lst = []
n = int(input())
for i in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))
lst.sort()
for i in lst:
    print(i)
