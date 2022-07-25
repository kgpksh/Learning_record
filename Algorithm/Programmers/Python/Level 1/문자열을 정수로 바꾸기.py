def solution(s):
    if s[0] == "+":
        return int(s[1:])
    elif s[0].isdigit():
        return int(s)
    else:
        return -int(s[1:])
