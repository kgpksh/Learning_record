from collections import Counter


def solution(s):
    c = Counter(s)
    p = c.get("p", 0) + c.get("P", 0)
    y = c.get("y", 0) + c.get("Y", 0)

    if p == y:
        return True
    else:
        return False
