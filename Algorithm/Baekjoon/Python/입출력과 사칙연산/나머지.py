i = input().split()
A = int(i[0])
B = int(i[1])
C = int(i[2])

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
