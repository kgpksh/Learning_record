s=set()
d={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
answer=True
a1=input()
a2=d[a1[0]]
a3=int(a1[1])
s.add(a1)

tmp1=a2
tmp2=a3

for _ in range(34):
    k=input()
    s.add(k)
    t1=d[k[0]]
    t2=int(k[1])
    if not ((abs(t1-tmp1)==2 and abs(t2-tmp2)==1) or (abs(t1-tmp1)==1 and abs(t2-tmp2)==2)):
        answer=False
    tmp1=t1
    tmp2=t2
    
b1=input()
b2=d[b1[0]]
b3=int(b1[1])
s.add(b1)

if len(s)!=36:
    answer=False
if not ((abs(b2-tmp1)==2 and abs(b3-tmp2)==1) or (abs(b2-tmp1)==1 and abs(b3-tmp2)==2)):
    answer=False
if not ((abs(b2-a2)==2 and abs(b3-a3)==1) or (abs(b2-a2)==1 and abs(b3-a3)==2)):
    answer=False
    
if answer:
    print('Valid')
else:
    print('Invalid')