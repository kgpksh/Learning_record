from fractions import Fraction as fr


def fac(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


m, n = map(int, input().split())
son = fac(m)
mother = fr((fac(n) * fac(m - n)))
answer = fr(son, mother) % 10007
print(answer)
