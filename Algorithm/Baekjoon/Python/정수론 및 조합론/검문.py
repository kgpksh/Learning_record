# a = A * K + R
# b = B * K + R ...
# b - a = (B - A) * K

from math import gcd
N = int(input())

nums = sorted([int(input()) for _ in range(N)])

numGap = []
for n in range(1, N) :
    numGap.append(nums[n] - nums[n - 1])
    
answer = set()
gap = gcd(*numGap)

answer.add(gap)
for g in range(2, int(gap ** 0.5) + 1) :
    if gap % g == 0 :
        answer.add(g)
        answer.add(gap // g)

print(*sorted(list(answer)))