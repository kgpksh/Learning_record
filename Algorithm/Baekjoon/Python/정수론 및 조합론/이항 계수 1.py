def fac(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


m, n = map(int, input().split())
print(int(fac(m) / (fac(n) * fac(m - n))))
