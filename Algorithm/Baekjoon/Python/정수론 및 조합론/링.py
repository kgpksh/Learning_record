from math import gcd

n = int(input())
l = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(l[0], l[i])
    print(str(int(l[0] / g)) + "/" + str(int(l[i] / g)))
