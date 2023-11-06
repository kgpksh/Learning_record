import sys
N = int(sys.stdin.readline().strip())
maY = -10000
miY = 10000
maX = -10000
miX = 10000

for _ in range(N) :
    x, y = map(int, sys.stdin.readline().strip().split())
    maX = max(maX, x)
    maY = max(maY, y)
    miX = min(miX, x)
    miY = min(miY, y)

print((maY - miY) * (maX - miX))