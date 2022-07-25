h, m = map(int, input().split())
time = int(input())

add = m + time
h += add // 60
if h > 24:
    h -= 24
m = add % 60

print(str(h) + " " + str(m))
