cnt=1
while True:
    n=int(input())
    if n==0:
        break
    L=[]
    bool=True
    for i in range(n):
        tmp=input()
        adder=[]
        for idx in range(len(tmp)):
            if tmp[idx]==' ':
                adder.append(tmp[:idx])
                adder.append(tmp[idx:].replace(' ',''))
                break
        L.append(adder)
        if 'N' in L[i][1]:
            bool=False
    print('Group '+str(cnt))
    if bool:
        print('Nobody was nasty')
    else:
        for g in range(n):
            for p in range(n-1):
                if L[g][1][p]=='N':
                    atk=L[g-(p+1)][0]
                    dfc=L[g][0]
                    print(atk+' was nasty about '+dfc)
    cnt+=1
    print('')