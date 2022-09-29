def solution(n):
    rec=[0]*(n+1)
    rec[1]=1
    for i in range(2,n+1):
        rec[i]=rec[i-2]+rec[i-1]
        
    return rec[n]%1234567