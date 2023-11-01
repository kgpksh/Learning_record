import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
answer = [str(i) for i in range(1, N + 1)]
for _ in range(M) :
    i, j= map(int, sys.stdin.readline().rstrip().split())
    cut = list(reversed(answer[i - 1 : j]))
    for idx in range(i - 1, j) :
        answer[idx] = cut[idx - i + 1]
print(' '.join(answer))