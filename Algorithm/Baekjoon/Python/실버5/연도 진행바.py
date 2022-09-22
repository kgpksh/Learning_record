month=['January','February','March','April','May','June','July','August','September','October','November','December']

m,d,y,hm=map(str,input().split())
m=month.index(m)+1
d=int(d[:-1])
y=int(y)
h,mi=map(int,hm.split(':'))

y_check=False
if (y%4==0 and y%100!=0) or y%400==0:
    y_check=True

all_m=365*1440
if y_check:
    all_m+=1440
    
ex=[0,31,28,31,30,31,30,31,31,30,31,30]
nowdays=sum(ex[:m])+d-1
if y_check and m>2:
    nowdays+=1

minute=nowdays*1440+h*60+mi
print((minute/all_m)*100)