import sys
from collections import deque

def p(dq) :
    if dq :
        return dq[-1]
    return -1

def pl(dq) :
    if dq :
        return dq.popleft()
    return -1

N = int(sys.stdin.readline().strip())
order = 1
line = deque(map(int, sys.stdin.readline().strip().split()))
stack = deque()

while line :
    stk = p(stack)    
    if stk == order :
        stack.pop()
        order += 1
        continue
    
    waiter = pl(line)
    if waiter == order :
        order += 1
        continue
        
    if waiter != -1 :
        stack.append(waiter)
         
while stack and stack.pop() == order :
    order += 1

if stack :
    print('Sad')
else :
    print('Nice')