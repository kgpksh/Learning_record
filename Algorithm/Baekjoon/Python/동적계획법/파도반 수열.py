tc = int(input())

for _ in range(tc):
    n = int(input())
    dpTable = [0] * 101
    dpTable[1] = 1
    dpTable[2] = 1
    dpTable[3] = 1
    dpTable[4] = 2
    dpTable[5] = 2
    if n < 4:
        print(1)
    elif n == 5:
        print(2)
    else:
        for i in range(6, n + 1):
            dpTable[i] = dpTable[i - 1] + dpTable[i - 5]
            
        print(dpTable[n])