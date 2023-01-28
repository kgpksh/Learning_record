import sys
string = list(sys.stdin.readline().rstrip())
explosive = list(sys.stdin.readline().rstrip())
l = len(explosive)

stk = []
for s in string:
    stk.append(s)
    if stk[-l :] == explosive:
        for _ in range(l):
            stk.pop()
        
if stk:
    print(''.join(stk))
else:
    print('FRULA')