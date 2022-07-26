from collections import Counter

a = int(input())
b = int(input())
c = int(input())
num = a * b * c

d = Counter(str(num))

for i in range(10):
    print(d.get(str(i), 0))
