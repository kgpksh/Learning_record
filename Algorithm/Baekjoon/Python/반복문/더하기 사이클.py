n = input()
if len(n) == 1:
    init = "0" + n
else:
    init = n


def cycle(n):
    if len(n) < 2:
        n = "0" + n
    a = n[-1]
    b = str(int(n[0]) + int(n[1]))

    return a + b[-1]


answer = 1

while True:
    m = cycle(n)
    if init == m:
        print(answer)
        break
    n = m
    answer += 1
