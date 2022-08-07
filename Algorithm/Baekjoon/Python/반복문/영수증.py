x = int(input())
n = int(input())

comparer = 0
for i in range(n):
    p, a = map(int, input().split())
    comparer += p * a
if x == comparer:
    print("Yes")
else:
    print("No")
