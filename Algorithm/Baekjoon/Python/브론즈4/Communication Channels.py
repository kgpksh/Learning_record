tc=int(input())
for _ in range(tc):
    a,b=map(str,input().split())
    if a==b:
        print('OK')
    else:
        print('ERROR')