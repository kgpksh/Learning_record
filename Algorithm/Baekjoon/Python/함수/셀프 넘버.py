def d(n):
    for s in str(n):
        n += int(s)
    return n


l = []
for i in range(1, 10001):
    l.append(d(i))

for i in range(1, 10001):
    if not i in l:
        print(i)
