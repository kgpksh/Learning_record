from collections import Counter
import sys

a = int(sys.stdin.readline())
sol = []
answer = 0
for i in range(a):
    sol.append(sys.stdin.readline())

for i in sol:
    s = list(set(i))
    check = False
    if len(i) == 1:
        answer + 1
        break
    for j in s:
        idx = []
        c = 0
        for k in range(len(i)):
            if j == i[k]:
                idx.append(k)

        z = zip(idx, idx[1:])
        for l, p in z:
            if p - l > 1:
                check = True
    if check == False:
        answer += 1
print(answer)
