import sys
n=int(input())
answer=-n+1
for _ in range(n):
    answer+=int(sys.stdin.readline().rstrip())
print(answer)