global count
count=0
tc=int(input())
def recursion(s, l, r):
    global count
    count+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)
 
for _ in range(tc):
    tmp=input()
    
    print(str(recursion(tmp,0,len(tmp)-1))+" "+str(count))
    count=0