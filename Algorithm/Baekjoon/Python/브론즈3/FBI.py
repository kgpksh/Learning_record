answer = []

for i in range(1, 6):
    fbi = input()
    
    if "FBI" in fbi:
        answer.append(str(i))
    
if answer:
    print(' '.join(answer))
else:
    print('HE GOT AWAY!')