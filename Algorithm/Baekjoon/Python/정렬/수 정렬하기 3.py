import sys

n = int(input())

tmp = [0] * 10000
for i in range(n):
    idx = int(sys.stdin.readline().rstrip())
    tmp[idx - 1] = tmp[idx - 1] + 1
for i in range(10000):
    if tmp[i] != 0:
        for j in range(tmp[i]):
            print(i + 1)
