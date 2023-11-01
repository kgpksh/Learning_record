import sys
N = int(sys.stdin.readline().rstrip())

L = []
for _ in range(N) :
  t = tuple(map(int, sys.stdin.readline().rstrip().split()))
  L.append(t)
L = sorted(L, key = lambda x : (x[1], x[0]))

answer = 0
E = 0
for s, e in L :
  if s >= E :
    answer += 1
    E = e
    
print(answer)