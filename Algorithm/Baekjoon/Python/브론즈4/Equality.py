k,c=map(str,input().split(' = '))
a,b=map(int,k.split(' + '))
if str(a+b)==c:
    print('YES')
else:
    print('NO')