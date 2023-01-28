def w(a,b,c, dpTable):
    if a > 20 or b > 20 or c > 20:
        dpTable[20][20][20] = w(20,20,20,dpTable)
        return dpTable[20][20][20]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if dpTable[a][b][c] != 1:
        return dpTable[a][b][c]
    
    if a < b and b < c:
        dpTable[a][b][c] = w(a, b, c-1, dpTable) + w(a, b-1, c-1, dpTable) - w(a, b-1, c, dpTable)
        return dpTable[a][b][c]


    dpTable[a][b][c] = w(a-1, b, c, dpTable) + w(a-1, b-1, c, dpTable) + w(a-1, b, c-1, dpTable) - w(a-1, b-1, c-1, dpTable)
    return dpTable[a][b][c]


def dpTable():
    return [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def printer(a,b,c,n):
    print('w({0}, {1}, {2}) = {3}'.format(a,b,c,n))

while True:
    a,b,c = map(int, input().split())
    
    if a == b == c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        printer(a,b,c,1)
    else:
        printer(a,b,c,w(a,b,c,dpTable()))