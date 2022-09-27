a,b,c=map(int,input().split())
s=set([a,b,c])
check=False
if len(s)<=2:
    check=True
else:
    tmp=sorted([a,b,c])
    if tmp[2]==tmp[0]+tmp[1]:
        check=True
if check:
    print('S')
else:
    print('N')