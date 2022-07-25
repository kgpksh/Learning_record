def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s):
            answer += 1
        s = s[1:] + s[0]

    return answer


def check(s):
    stk = []
    for i in s:
        if i in ["[", "{", "("]:
            stk.append(i)
        elif stk and i in ["]", "}", ")"]:
            if i == "]" and stk[-1] == "[":
                stk.pop()
            elif i == "}" and stk[-1] == "{":
                stk.pop()
            elif i == ")" and stk[-1] == "(":
                stk.pop()
        else:
            stk.append(i)

    if stk:
        return False
    else:
        return True
