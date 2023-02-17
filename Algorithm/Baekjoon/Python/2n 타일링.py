a = 1
b = 2

n = int(input())
if n == 1 :
        print(1)
elif n == 2:
    print(2)
else:
    for i in range(3, n + 1):
            tmp = (a + b) % 10007
            a = b
            b = tmp
    print(b)