a=[]
a.append([0])

for _ in range(5):
    a[0][0] = a[0][0] + 1

print(a)