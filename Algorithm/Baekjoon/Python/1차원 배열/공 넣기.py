import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
answer = ['0'] * N

for _ in range(M) :
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    for idx in range(i - 1, j) :
        answer[idx] = str(k)
        
print(' '.join(answer))