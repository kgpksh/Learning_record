import sys
from math import lcm

def solve() :
    a, b, c, d, e, f = map(int, sys.stdin.readline().strip().split())
    if a == 0 :
        y = c // b
        x = (f - (e * y)) // d
        return (str(x) + ' ' + str(y))
    
    if d == 0 :
        y = f // e
        x = (c - (b * y)) // a
        return (str(x) + ' ' + str(y))
    L = lcm(a, d)
    B = b * (L // a)
    C = c * (L // a)
    E = e * (L // d)
    F = f * (L // d)
    if (B - E) == 0 :
        return ('0 0')
    y = (C - F) // (B - E)
    x = (c - b * y) // a

    return (str(x) + ' ' + str(y))

print(solve())