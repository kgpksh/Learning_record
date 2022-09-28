a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
answer=0
if a1-a2<0:
    answer+=abs(a1-a2)
if b1-b2<0:
    answer+=abs(b1-b2)
if c1-c2<0:
    answer+=abs(c1-c2)
print(answer)