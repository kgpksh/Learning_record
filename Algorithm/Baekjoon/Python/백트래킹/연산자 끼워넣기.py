from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
calculator = list(map(int, input().split()))

calculators = []
for _ in range(calculator[0]):
    calculators.append('+')
for _ in range(calculator[1]):
    calculators.append('-')
for _ in range(calculator[2]):
    calculators.append('*')
for _ in range(calculator[3]):
    calculators.append('%')
    
big = -1000000001
small = 1000000001
allPossible = list(permutations(calculators, n - 1))
allPossible = list(set(allPossible))
for per in allPossible:
    answer = numbers[0]
    for i in range(n - 1):
        if per[i] == '+':
            answer += numbers[i + 1]
        elif per[i] == '-':
            answer -= numbers[i + 1]
        elif per[i] == '*':
            answer *= numbers[i + 1]
        else:
            if answer < 0:
                answer = -((-answer) // numbers[i + 1])
            else:
                answer //= numbers[i + 1]
    big = max(big, answer)
    small = min(small, answer)

print(big)
print(small)