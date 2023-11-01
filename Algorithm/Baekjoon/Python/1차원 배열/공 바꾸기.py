import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
answer = [str(i) for i in range(1, N + 1)]
for _ in range(M) :
    i, j= map(int, sys.stdin.readline().rstrip().split())
    tmp = answer[i - 1]
    answer[i - 1] = answer[j - 1]
    answer[j - 1] = tmp

print(' '.join(answer))