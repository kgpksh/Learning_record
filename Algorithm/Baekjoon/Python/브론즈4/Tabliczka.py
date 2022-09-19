m,n=map(int,input().split())
v=m//2
a=abs((v*n)-(m-v)*n)
h=n//2
b=abs((h*m)-(n-h)*m)
print(min(a,b))