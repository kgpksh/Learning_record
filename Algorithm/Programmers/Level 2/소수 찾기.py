from itertools import permutations


def solution(numbers):
    s = set()
    length = len(numbers)
    for l in range(1, length + 1):
        for c in permutations(numbers, l):
            i = int("".join(c))
            if prime(i):
                s.add(i)
    return len(s)


def prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int((n / 2)) + 1):
        if n % i == 0:
            return False
    return True
