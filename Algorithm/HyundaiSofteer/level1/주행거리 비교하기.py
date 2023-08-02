import sys

def solution() :
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a > b :
        return 'A'
    
    if a < b :
        return 'B'

    return 'same'

print(solution())