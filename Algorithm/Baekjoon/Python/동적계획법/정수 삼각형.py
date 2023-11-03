import sys
n = int(sys.stdin.readline().rstrip())
triangle = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for idx in range(1, n) :
    triangle[idx][0] += triangle[idx - 1][0]
    triangle[idx][idx] += triangle[idx - 1][idx - 1]
    for row in range(1, idx) :
        triangle[idx][row] += max(triangle[idx - 1][row - 1], triangle[idx - 1][row])
        
print(max(triangle[n - 1]))