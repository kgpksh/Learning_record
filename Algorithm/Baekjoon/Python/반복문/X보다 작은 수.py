import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))

answer = []
for i in a:
    if i < x:
        answer.append(str(i))
print(" ".join(answer))
