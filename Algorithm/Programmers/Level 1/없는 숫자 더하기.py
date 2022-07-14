def solution(numbers):
    all = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    s = set(numbers)
    return sum(list(all - s))
