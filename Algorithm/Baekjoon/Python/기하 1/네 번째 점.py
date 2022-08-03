a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

x = {}
y = {}
x[a[0]] = x.get(a[0], 0) + 1
x[b[0]] = x.get(b[0], 0) + 1
x[c[0]] = x.get(c[0], 0) + 1
y[a[1]] = y.get(a[1], 0) + 1
y[b[1]] = y.get(b[1], 0) + 1
y[c[1]] = y.get(c[1], 0) + 1

print(
    str(sorted(x.items(), key=lambda x: x[1])[0][0])
    + " "
    + str(sorted(y.items(), key=lambda x: x[1])[0][0])
)
