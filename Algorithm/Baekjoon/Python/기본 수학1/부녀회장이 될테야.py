tc = int(input())

for i in range(tc):

    k = int(input())
    n = int(input())
    tmp = [[i + 1 for i in range(n)]]

    for j in range(k):
        row = []
        for h in range(1, n + 1):
            row.append(sum(tmp[j][:h]))
        tmp.append(row)

    print(tmp[k][n - 1])
