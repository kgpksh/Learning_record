from collections import Counter as c
s=input()
L=[0]*26
cnt=c(s)
for i in range(26):
    L[i]=str(cnt.get(chr(i+ord('a')),0))
print(' '.join(L))