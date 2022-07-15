def solution(s):
    l = len(s)
    if l % 2 == 0:
        d = int(l / 2)
        return s[d - 1 : d + 1]
    else:
        return s[l // 2]
