from math import log2
def solution(n,a,b):
    k=int(log2(n))
    j=min(a,b)
    h=max(a,b)
    start=1
    end=n
    
    for i in range(k):
        tmp=(end-(start-1))//2
        tmp2=start+tmp
        if start<=j<tmp2 and tmp2<=h<=end:
            return k-i
        elif j<tmp2 and h<tmp2:
            end=tmp2-1
        elif j>=tmp2 and h>=tmp2:
            start=tmp2