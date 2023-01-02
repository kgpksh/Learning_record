from math import pi
cnt = 1

while True:
    r, n, t = map(float, input().split())
    if n == 0:
        break
        
    d = r * pi * n / 63360
    speed = d / (t / 3600)
    
    print('Trip #{0}: {1} {2}'.format(cnt, format(round(d, 2), '.2f'), format(round(speed, 2), '.2f')))
    cnt +=1