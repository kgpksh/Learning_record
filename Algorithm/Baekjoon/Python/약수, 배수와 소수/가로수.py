import sys
from math import gcd

N = int(sys.stdin.readline().strip())
trees = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])
distance = trees[1] - trees[0]

for t in range(2, N) :
    distance = gcd(distance, trees[t] - trees[t - 1])
    
print((trees[-1] - trees[0]) // distance - N + 1)