def solution(s):
    S=list(s)
    S[0]=S[0].upper()
    for i in range(1,len(S)):
        if S[i-1]==' ':
            S[i]=S[i].upper()
        else:
            S[i]=S[i].lower()
    return ''.join(S)