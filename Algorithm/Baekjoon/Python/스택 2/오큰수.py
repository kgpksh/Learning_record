import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
a = deque(enumerate(A))
    
stk = []
answer = ['-1'] * n

while a :
    if not stk :
        stk.append(a.popleft())
        continue
    
    while stk and stk[-1][1] < a[0][1] :
        answer[stk[-1][0]] = str(a[0][1])
        stk.pop()
    stk.append(a.popleft())
    
print(' '.join(answer))