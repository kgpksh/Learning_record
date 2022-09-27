a,b,c=map(int,input().split())

if a==b==c:
    print('*')
else:
    if a==b:
        print('C')
    elif a==c:
        print('B')
    else:
        print('A')