import sys

n = int(input())
lst = set()
for i in range(n):
    word = sys.stdin.readline().rstrip()
    lst.add(word)

s = []
for i in lst:
    s.append([i, len(i)])
s.sort(key=lambda x: (x[1], x[0]))

for i in s:
    print(i[0])
