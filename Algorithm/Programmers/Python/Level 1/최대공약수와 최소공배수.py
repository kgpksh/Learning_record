def solution(n, m):
    aa = a(n, m)
    bb = int(n * m / aa)
    return [aa, bb]


def a(n, m):
    mm = max(n, m)
    mn = min(n, m)
    div = mm % mn
    if mm / mn == mm:
        return 1

    if div == 0:
        return mn
    else:
        return a(mn, div)
