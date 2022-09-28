n=input()
if '10' in n:
    if n.count('0')==2:
        print(20)
    else:
        if n[1]=='0':
            print(10+int(n[2]))
        else:
            print(10+int(n[0]))
else:
    print(int(n[0])+int(n[1]))