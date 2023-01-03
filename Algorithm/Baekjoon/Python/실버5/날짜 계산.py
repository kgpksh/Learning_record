from collections import deque
e, s, m = map(int,input().split())

earth = deque([i for i in range(1, 16)])
sun = deque([i for i in range(1, 29)])
moon = deque([i for i in range(1, 20)])
answer = 1

while True:
    a = earth[0]
    b = sun[0]
    c = moon[0]
    
    if a == e and b == s and c == m:
        break

    earth.rotate(-1)
    sun.rotate(-1)
    moon.rotate(-1)
    answer +=1
print(answer)