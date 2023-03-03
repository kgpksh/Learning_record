a, b = map(int, input().split())
answer = 0

while a != b :
    if b < a :
        answer = -1
        break
        
    if b % 2 == 0 :
        b //= 2
        answer += 1
        continue
       
    if str(b)[-1] == '1' :
        b = (b - 1) // 10
        answer += 1
        continue
        
    answer = -1
    break

if answer != -1 :
    print(answer + 1)
else : 
    print(-1)