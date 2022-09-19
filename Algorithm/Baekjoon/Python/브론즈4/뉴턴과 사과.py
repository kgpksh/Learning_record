L=input().split()
x,_,_=map(str,input().split())
try:
    print(L.index(x)+1)
except:
    print(0)