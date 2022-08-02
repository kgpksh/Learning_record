from collections import Counter
from math import trunc
import sys

case = int(input())
lst = []


for i in range(case):
    lst.append(int(sys.stdin.readline()))

lst.sort()
d = sorted(list(Counter(lst).items()), key=lambda x: (-x[1], x[0]))

print(round(sum(lst) / case))

print(lst[trunc(case / 2)])


if case == 1:
    print(d[0][0])
elif d[0][1] == d[1][1]:
    print(d[1][0])
else:
    print(d[0][0])

print(max(lst) - min(lst))
