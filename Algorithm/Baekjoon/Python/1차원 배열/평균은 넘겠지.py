import sys

n = int(input())
for i in range(n):
    arr = sys.stdin.readline().split()
    s = 0
    for a in range(1, int(arr[0]) + 1):
        s += int(arr[a])

    avg = s / int(arr[0])
    n = 0

    for j in range(1, int(arr[0]) + 1):
        if int(arr[j]) > avg:
            n += 1
    answer = n / int(arr[0]) * 100
    print(f"{answer:.3f}%")
