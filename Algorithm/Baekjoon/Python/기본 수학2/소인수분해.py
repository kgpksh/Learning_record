i = int(input())
while i != 1:
    for j in range(2, i + 1):
        if i % j == 0:
            print(j)
            i = int(i / j)
            break
