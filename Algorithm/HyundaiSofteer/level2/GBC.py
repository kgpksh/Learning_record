import sys

safe, real = map(int, sys.stdin.readline().rstrip().split())

def recordFloors(cases) :
    result = [0] * 100
    lastStandard = 0

    for _ in range(cases) :
        height, speed = map(int, sys.stdin.readline().rstrip().split())

        for floor in range(lastStandard, lastStandard + height) :
            result[floor] = speed
        
        lastStandard += height

    return result

safeStandard = recordFloors(safe)
realCase = recordFloors(real)

answer = 0

for idx in range(100) :
    answer = max(answer, realCase[idx] - safeStandard[idx])
print(answer)