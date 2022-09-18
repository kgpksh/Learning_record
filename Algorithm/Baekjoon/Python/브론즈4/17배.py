n=input()
tmp=''.join(reversed(n))
a=0
for i in range(len(n)):
    a+=(2**i)*int(tmp[i])
print(bin(a*17)[2:])