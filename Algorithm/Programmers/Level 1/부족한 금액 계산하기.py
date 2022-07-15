def solution(price, money, count):
    answer = -1
    p = 0
    for i in range(1, count + 1):
        p += price * i
    if money > p:
        return 0
    else:
        return p - money
