tc = int(input())

for _ in range(tc):
    answer = []
    money = int(input())
    
    answer.append(str(money // 25))
    money %= 25
    
    answer.append(str(money // 10))
    money %= 10
    
    answer.append(str(money // 5))
    money %= 5

    answer.append(str(money))
    
    print(' '.join(answer))