n = int(input())
subjects = list(map(int, input().split()))
m = max(subjects)
tmp = 0
for i in subjects:
    tmp += i * 100 / m
print(tmp / n)
