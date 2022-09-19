s=[]
m=[]
for _ in range(4):
    s.append(int(input()))
for _ in range(2):
    m.append(int(input()))
s.sort()
m.sort()
print(sum(s[1:])+m[1])