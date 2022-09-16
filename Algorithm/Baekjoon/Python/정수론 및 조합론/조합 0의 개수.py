n,m=map(int,input().split())
def divide(n,d):
    e=0
    result=0
    while True:
        if d**(e+1)>n:
            break
        e+=1
    
    for i in range(1,e+1):
        result+=int(n/(d**i))
    return result

two=0
five=0
two+=divide(n,2)
five+=divide(n,5)
two-=divide(m,2)
five-=divide(m,5)
two-=divide(n-m,2)
five-=divide(n-m,5)
print(min(two,five))