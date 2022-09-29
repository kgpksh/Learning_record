def solution(S):
    check=[]
    for s in S:
        if s=='(':
            check.append(s)
        else:
            if check and check[-1]=='(':
                check.pop()
            else:
                return False
    if check:
        return False
    else:
        return True