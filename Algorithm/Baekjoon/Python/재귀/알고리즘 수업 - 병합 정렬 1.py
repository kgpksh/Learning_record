m,k=map(int,input().split())
lst=list(map(int,input().split()))
global A, answer, K,cnt
K=k
A=[0 for i in range(m)]
answer=-1
cnt=0
def merge(a,p,middle,q):
    global A,K, answer,cnt
    i=p
    j=middle+1
    r=p
    while i<=middle and j<=q:
        if a[i]<=a[j]:
            cnt+=1
            A[r]=a[i]
            if K==cnt:
                    answer=a[i]
            i+=1
        else:
            cnt+=1
            A[r]=a[j]
            if K==cnt:
                    answer=a[j]
            j+=1
        r+=1
        
        
    if i>middle:
        for tmp in range(j,q+1):
            cnt+=1
            A[r]=a[tmp]
            if K==cnt:
                answer=a[tmp]
            r+=1
    else:
        for tmp in range(i,middle+1):
            cnt+=1
            A[r]=a[tmp]
            if K==cnt:
                answer=a[tmp]
            r+=1
    
    for t in range(p,q+1):
        a[t]=A[t]
            
def merge_sort(a,m,n):
    if m<n:
        middle=(m+n)//2
        merge_sort(a,m,middle)
        merge_sort(a,middle+1,n)
        merge(a,m,middle,n)
        
        
merge_sort(lst,0,m-1)
print(answer)