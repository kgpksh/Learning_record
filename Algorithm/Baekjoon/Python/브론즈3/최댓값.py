table = []

highest = 0
r = 0
c = 0

for _ in range(9):
    table.append(list(map(int, input().rstrip().split(' '))))
    
for i in range(9):
    for j in range(9):
        tmp = table[i][j]
        if highest < tmp:
            highest = tmp
            r = i
            c = j
            
print(highest)
print(str(r + 1) + ' ' + str(c + 1))