import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
W = list(map(int,sys.stdin.readline().rstrip().split()))
record = {}
for person in range(1, N + 1) :
  record[person] = -1
  
for i in range(M) :
  A, B = map(int, sys.stdin.readline().rstrip().split())
  
  record[A] = max(record[A], W[B - 1])
  record[B] = max(record[B], W[A - 1])
  
answer = 0
for k, v in record.items() :
  if W[k - 1] > v :
    answer += 1
print(answer)