import sys

w, h, x, y, p = map(int, sys.stdin.readline().rstrip().split())

answer = 0
for i in range(p):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a >= x and a <= x + w and b >= y and b <= y + h:
        answer += 1

    elif a < x:
        if abs(x - a) ** 2 + abs(b - (y + (h / 2))) ** 2 <= (h / 2) ** 2:
            answer += 1
    elif a > x + w:
        if abs((x + w) - a) ** 2 + abs(b - (y + (h / 2))) ** 2 <= (h / 2) ** 2:
            answer += 1
print(answer)
