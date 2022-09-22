y1, m1, d1=map(int,input().split())
y2, m2, d2=map(int,input().split())

def check(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        return True
    return False

def mtd(y,m):
    ex=[0,31,28,31,30,31,30,31,31,30,31,30]
    if check(y):
        ex[2]=29
    return sum(ex[:m])
day1=(y1-1)*365+((y1-1)//4)-((y1-1)//100)+((y1-1))//400+mtd(y1,m1)+d1
day2=(y2-1)*365+((y2-1))//4-((y2-1)//100)+((y2-1))//400+mtd(y2,m2)+d2

gap=day2-day1
if y1+1000<y2:
    print('gg')
elif y1+1000==y2:
    if m2>m1:
        print('gg')
    elif m1==m2:
        if d2>=d1:
            print('gg')
        else:
            print('D-'+str(gap))
    else:
        print('D-'+str(gap))
else:
    print('D-'+str(gap))   