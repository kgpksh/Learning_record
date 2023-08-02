import sys

w, n = map(int, sys.stdin.readline().rstrip().split())

jewels = []

for _ in range(n) :
    m, p = map(int, sys.stdin.readline().rstrip().split())

    jewels.append((m, p))

jewels = sorted(jewels, key = lambda x : -x[1])

answer = 0

for jewel in jewels :
    m, p = jewel

    addedWeight = min(w, m)

    answer += addedWeight * p
    w -= addedWeight

    if w == 0:
        break

print(answer)