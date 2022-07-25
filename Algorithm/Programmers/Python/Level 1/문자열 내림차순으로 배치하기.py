def solution(s):
    s = sorted(s, reverse=True)
    ss = ""
    for i in s:
        ss += i
    return ss
