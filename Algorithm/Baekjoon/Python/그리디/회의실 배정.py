from collections import deque

n = int(input())

schedule = []

for _ in range(n) :
    s, e = map(int, input().split())
    
    schedule.append((s, e))
    
schedule = sorted(schedule, key = lambda x : (x[1], x[0]))

now = 0
answer = 0
for sc in schedule :
    s, e = sc
    
    if s >= now :
        answer += 1
        now = e
        
print(answer)