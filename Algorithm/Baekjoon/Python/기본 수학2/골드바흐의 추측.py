def check(n):
    if n == 1:
        return False
    d = int(n**0.5)
    for i in range(2, d + 1):
        if n % i == 0:
            return False
    return True


def adder(a, b):
    if check(a) and check(b):
        return a
    else:
        return adder(a - 1, b + 1)


tc = int(input())
for i in range(tc):
    n = int(input())
    if check(n / 2):
        print(str(int(n / 2)) + " " + str(int(n / 2)))
    else:
        j = adder(n / 2, n / 2)
        print(str(int(j)) + " " + str(int(n - j)))
