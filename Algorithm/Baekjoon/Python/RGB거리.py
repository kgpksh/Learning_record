numberOfHouse = int(input())
colorArr = [[0,0,0]]
dpTable = [[0, 0, 0] for _ in range(numberOfHouse + 1)]

for _ in range(numberOfHouse):
    colorArr.append(list(map(int, input().split())))

for house in range(1, numberOfHouse + 1):
    dpTable[house][0] = min(dpTable[house - 1][1], dpTable[house - 1][2]) + colorArr[house][0]
    dpTable[house][1] = min(dpTable[house - 1][0], dpTable[house - 1][2]) + colorArr[house][1]
    dpTable[house][2] = min(dpTable[house - 1][0], dpTable[house - 1][1]) + colorArr[house][2]
    
print(min(dpTable[-1]))