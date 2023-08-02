k, p, n = map(int, input().rstrip().split())

while n > 0:
    if n % 2 != 0:
        k = (k * p) % 1000000007
    n //= 2
    p = (p * p) % 1000000007

print(k)