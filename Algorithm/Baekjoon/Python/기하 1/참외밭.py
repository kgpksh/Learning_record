from collections import deque

n=int(input())

length=deque()
for _ in range(6):
    _, l=map(int, input().split())
    length.append(l)
max_idx=length.index(max(length))
length.rotate(3-max_idx)

direction=0
full_size=0
if length[2]>=length[4]:
    full_size=length[3]*length[2]
    direction=5
else:
    full_size=length[3]*length[4]
    direction=1

print(n*(full_size-(length[direction]*length[0])))