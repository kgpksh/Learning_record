import sys

T = int(sys.stdin.readline().rstrip())

for case in range(T) :
    answer = str(sum(map(int, sys.stdin.readline().rstrip().split())))
    prefix = 'Case #'+ str(case + 1) +': '
    print(prefix + answer)