import sys
from collections import deque

N = int(sys.stdin.readline().strip())

L = 0
stk = deque()
for _ in range(N) :
    command = sys.stdin.readline().strip()
    if command[0] == '1' :
        stk.append(command[2:])
        L += 1
        continue
        
    if command == '2' :
        if L > 0 :
            print(stk.pop())
            L -= 1
            continue
        print(-1)
        continue
    
    if command == '3' :
        print(L)
        continue
        
    if command == '4' :
        if L > 0 :
            print(0)
            continue
        print(1)
        continue
        
    if L > 0 :
        print(stk[-1])
        continue
    print(-1)