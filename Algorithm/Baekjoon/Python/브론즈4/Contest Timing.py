import datetime
dt1 = datetime.datetime(2011, 11, 11, 11, 11)
d,h,m=map(int,input().split())
dt2 = datetime.datetime(2011, 11, d, h, m)
td = dt2 - dt1
s=td.total_seconds()
if s<0:
    print(-1)
else:
    print(int(s/60))