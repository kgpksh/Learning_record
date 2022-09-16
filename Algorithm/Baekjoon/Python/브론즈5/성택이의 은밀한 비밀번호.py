tc=int(input())
for _ in range(tc):
    password=len(input())
    if password>=6 and password<=9:
        print('yes')
    else:
        print('no')