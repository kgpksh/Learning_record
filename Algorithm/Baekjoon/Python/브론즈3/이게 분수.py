def rotate(table):
    tmp = table[0][1]
    table[0][1] = table[0][0]
    table[0][0] = table[1][0]
    table[1][0] = table[1][1]
    table[1][1] = tmp
    
    return table

table = []
for _ in range(2):
    table.append(list(map(int, input().split())))
    
r = 0
m = table[0][0] / table[1][0] + table[0][1] / table[1][1]

for i in range(1, 4):
    table = rotate(table)
    calculated = table[0][0] / table[1][0] + table[0][1] / table[1][1]
    
    if m < calculated :
        r = i
        m = calculated

print(r)