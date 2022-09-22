import sys
for _ in range(3):
    n=int(sys.stdin.readline().rstrip())
    answer=0
    for _ in range(n):
        answer+=int(sys.stdin.readline().rstrip())
    if answer==0:
        print(0)
    elif answer>0:
        print('+')
    else:
        print('-')