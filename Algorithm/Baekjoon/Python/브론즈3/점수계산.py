l=input()
a=input()
a=a.replace(' ','')
L=a.split('0')
answer=0
for s in L:
    n=len(s)
    answer+=(n*(n+1))//2
print(answer)