a=input()
b=input()
A=0
B=0
idx=0
for i in reversed(a):
    A+=int(i)*(2**idx)
    idx+=1
idx=0
for i in reversed(b):
    B+=int(i)*(2**idx)
    idx+=1
print(bin(A*B)[2:])