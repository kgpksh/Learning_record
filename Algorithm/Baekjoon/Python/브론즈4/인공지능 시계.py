h,m,s=map(int,input().split())
time=int(input())
tmp=h*3600+m*60+s+time
a=int((tmp%86400)/3600)
b=((tmp%86400)%3600)//60
c=((tmp%86400)%3600)%60
print(str(a)+" "+str(b)+" "+str(c))