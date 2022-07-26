idx = 1
fore = 0
for i in range(1, 10):
    next = int(input())
    if max(fore, next) == next:
        idx = i
        fore = next
print(fore)
print(idx)
