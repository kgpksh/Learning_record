s,k,h=map(int,input().split())
D={s:'Soongsil',k:'Korea',h:'Hanyang'}
if s+k+h>=100:
    print('OK')
else:
    print(D[min(s,k,h)])