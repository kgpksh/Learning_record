from math import lcm
from math import gcd

a, b = map(int, input().split())
c, d = map(int, input().split())

L = lcm(b, d)
A = a * (L // b) + c * (L // d)

g = gcd(A, L)
print(A // g)
print(L // g)