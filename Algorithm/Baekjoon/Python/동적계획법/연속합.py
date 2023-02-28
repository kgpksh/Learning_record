n = int(input())
dpTable = list(map(int, input().split()))

for i in range(1, n) :
    dpTable[i] = max(dpTable[i] + dpTable[i - 1], dpTable[i])
    
print(max(dpTable))