import sys

t = int(input())

for i in range(t):
    print(
        "Case #{0}: {1}".format(
            i + 1, sum(map(int, sys.stdin.readline().rstrip().split()))
        )
    )
