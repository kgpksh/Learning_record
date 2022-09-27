x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
X1=min(x1,x2,x3,x4)
Y1=min(y1,y2,y3,y4)
X2=max(x1,x2,x3,x4)
Y2=max(y1,y2,y3,y4)

print(max((X2-X1),(Y2-Y1))**2)