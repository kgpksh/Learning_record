i = input().split()
a = "".join(reversed(i[0]))
b = "".join(reversed(i[1]))
print(max(int(a), int(b)))
