import sys

n = int(input())
lst = []

for i in range(n):
    a, b = sys.stdin.readline().split()
    lst.append([int(a), b])

lst.sort(key=lambda x: x[0])
for i in lst:
    print(str(i[0]) + " " + i[1])
