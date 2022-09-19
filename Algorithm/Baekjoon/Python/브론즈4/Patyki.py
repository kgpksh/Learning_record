t=list(map(int,input().split()))
t.sort()
if t[0]==t[1]==t[2]:
    print(2)
elif t[0]**2+t[1]**2==t[2]**2:
    print(1)
else:
    print(0)