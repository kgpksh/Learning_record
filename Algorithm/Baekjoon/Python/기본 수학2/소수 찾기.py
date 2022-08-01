def check(n):
    if n == 1:
        return False
    d = int(n**0.5)
    for i in range(2, d + 1):
        if n % i == 0:
            return False
    return True


a = input()
numbers = list(map(int, input().split()))
cnt = 0
for i in numbers:
    if check(i):
        cnt += 1
print(cnt)
