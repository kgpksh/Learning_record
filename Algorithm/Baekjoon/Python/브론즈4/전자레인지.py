a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

if a<0 and b<=0:
    print(c(b-a))
elif a<0 and b>0:
    print(abs(a*c)+d+b*e)
else:
    print(e*(b-a))