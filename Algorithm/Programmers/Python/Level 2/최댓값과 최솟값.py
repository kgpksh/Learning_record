def solution(s):
    L=list(map(int,s.split()))
    return str(min(L))+' '+str(max(L))