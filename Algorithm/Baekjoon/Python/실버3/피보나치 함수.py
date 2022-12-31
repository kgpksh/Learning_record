tc = int(input())

for _ in range(tc):
    zero = [1,0]
    one = [0,1]

    n = int(input())
    if n <2:
        print(str(zero[n]) + ' ' + str(one[n]))
        continue

    for i in range(2, n + 1):
        zero.append(zero[i - 2] + zero[i - 1])
        one.append(one[i - 2] + one[i - 1])
        
    print(str(zero[n]) + ' ' + str(one[n]))