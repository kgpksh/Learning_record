case = int(input())

for i in range(case):
    H, W, N = map(int, input().split())

    f = N % H
    h = N // H
    if f == 0:
        f = H
    else:
        h += 1
    h = str(h)
    if len(h) == 1:
        h = "0" + h

    print(str(f) + h)
