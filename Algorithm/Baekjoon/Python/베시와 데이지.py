b1,b2=map(int,input().split())
d1,d2=map(int,input().split())
j1,j2=map(int,input().split())

bx=abs(j1-b1)
by=abs(j2-b2)

dx=abs(j1-d1)
dy=abs(j2-d2)

b=max(bx,by)
d=dx+dy
if b==d:
    print('tie')
elif b<d:
    print('bessie')
else:
    print('daisy')