tc = int(input())

for t in range(tc):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    for n in range(int(input())):
        a, b, r = map(int, input().split())
        if (
            abs(x1 - a) ** 2 + abs(y1 - b) ** 2 < r**2
            and abs(x2 - a) ** 2 + abs(y2 - b) ** 2 < r**2
        ):
            pass
        elif (
            abs(x1 - a) ** 2 + abs(y1 - b) ** 2 < r**2
            or abs(x2 - a) ** 2 + abs(y2 - b) ** 2 < r**2
        ):
            answer += 1

    print(answer)
