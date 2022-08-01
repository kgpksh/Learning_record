def check(n):
    if n == 1:
        return False
    d = int(n**0.5)
    for i in range(2, d + 1):
        if n % i == 0:
            return False
    return True


m, n = map(int, input().split())
for i in range(m, n + 1):
    if check(i):
        print(i)
