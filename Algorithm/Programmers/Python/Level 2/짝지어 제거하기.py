def solution(S):
    stk=[]
    for s in S:
        if stk:
            if stk[-1]==s:
                stk.pop()
            else:
                stk.append(s)
        else:
            stk.append(s)
    if stk:
        return 0
    else:
        return 1
        