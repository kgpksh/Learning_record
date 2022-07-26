import sys


def readline():
    return sys.stdin.readline().rstrip()


t = int(readline())
l = list(map(int, readline().split()))

print(min(l), max(l))
