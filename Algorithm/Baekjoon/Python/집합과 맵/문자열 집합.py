import sys

n, m = map(int, input().split())
s = {}
for i in range(n):
    s[sys.stdin.readline().rstrip()] = 1

answer = 0
for i in range(m):
    answer += s.get(sys.stdin.readline().rstrip(), 0)

print(answer)
