import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == "0 0":
        break
    print(sum(map(int, s.split())))
