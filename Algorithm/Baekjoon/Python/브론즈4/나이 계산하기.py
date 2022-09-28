y1,m1,d1=map(int,input().split())
y2,m2,d2=map(int,input().split())

if y1==m1:
    print(0)
else:
    if m2<m1:
        print(y2-y1-1)
    elif m1==m2:
        if d2<d1:
            print(y2-y1-1)
        else:
            print(y2-y1)
    else:
        print(y2-y1)
        
print(y2-y1+1)

print(y2-y1)