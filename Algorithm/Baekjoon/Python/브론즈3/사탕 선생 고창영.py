import sys
tc=int(sys.stdin.readline().rstrip())
sys.stdin.readline().rstrip()
for t in range(tc):
    n=int(sys.stdin.readline().rstrip())
    tmp=0
    for i in range(n):
        tmp+=int(sys.stdin.readline().rstrip())
    if tmp%n==0:
        print('YES')
    else:
        print('NO')
    if t!=tc-1:
        sys.stdin.readline().rstrip()