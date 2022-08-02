import sys

n = int(input())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
d = dict.fromkeys(cards, "1")
m = int(input())
question = list(map(int, sys.stdin.readline().rstrip().split()))

for q in range(m):
    if q == m - 1:
        print(d.get(question[q], 0))
    else:
        print(d.get(question[q], 0), end=" ")
