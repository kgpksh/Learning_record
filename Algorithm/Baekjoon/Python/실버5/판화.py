size = int(input())
moving = input()

converter = {"R" : 1, "L" : -1, 'U': 1, 'D': -1}
recorder = {"R" : 'R', 'L' : 'R', 'U': 'U', "D" : 'U'}
board = []
for _ in range(size):
    tmp = []
    for _ in range(size):
        tmp.append(set())
    board.append(tmp)

x = 0
y = size
for m in moving:
    tmpx = x
    tmpy = y
    if m in ["R", "L"]:
        tmpx += converter[m]
    elif m in ["U", "D"]:
        tmpy += converter[m]
        
    if tmpx < 0 or tmpx >= size or tmpy > size or tmpy < 1:
        continue

    board[size - y][x].add(recorder[m])
    board[size - tmpy][tmpx].add(recorder[m])
    x = tmpx
    y = tmpy
       
answer = []
for a in board:
    tmp = []
    for b in a:
        if len(b) == 2:
            tmp.append('+')
        elif len(b) == 0:
            tmp.append('.')
        elif list(b)[0] in ['R', 'L']:
            tmp.append('-')
        else:
            tmp.append('|')
    answer.append(tmp)

for b in answer:
    print(''.join(b))