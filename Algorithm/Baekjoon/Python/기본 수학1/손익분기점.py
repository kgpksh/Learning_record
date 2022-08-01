import math

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    d = a / (c - b)
    e = math.ceil(d)
    if e == int(d):
        print(e + 1)
    else:
        print(e)
