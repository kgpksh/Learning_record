def check(n):
    if n == 1:
        return False
    d = int(n**0.5)
    for i in range(2, d + 1):
        if n % i == 0:
            return False
    return True


M = int(input())
N = int(input())

lst = []
for i in range(M, N + 1):
    if check(i):
        lst.append(i)
if not lst:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
