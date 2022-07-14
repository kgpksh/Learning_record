def solution(a, b):
    lst = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day = 0
    if a != 1:
        for i in range(1, a):
            day += days(i)
    day += b - 1
    return lst[day % 7]


def days(m):
    if m == 2:
        return 29
    elif m >= 1 and m <= 7:
        if m % 2 == 1:
            return 31
        else:
            return 30
    else:
        if m % 2 == 1:
            return 30
        else:
            return 31
