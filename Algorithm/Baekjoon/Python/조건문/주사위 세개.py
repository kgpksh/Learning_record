i = input().split()
j = []
for a in i:
    j.append(int(a))
s = set(j)

if len(s) == 1:
    print(10000 + j[0] * 1000)
elif len(s) == 2:
    if j[0] == j[1]:
        print(1000 + j[0] * 100)
    elif j[0] == j[2]:
        print(1000 + j[0] * 100)
    else:
        print(1000 + j[1] * 100)
else:
    print(100 * max(j))
