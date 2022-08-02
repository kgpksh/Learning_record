import sys
from collections import Counter

m = int(sys.stdin.readline().rstrip())
cards = Counter(sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
question = sys.stdin.readline().rstrip().split()

answer = ""
for q in range(n):
    if q == n - 1:
        print(cards.get(question[q], 0))
    else:
        print(cards.get(question[q], 0), end=" ")
