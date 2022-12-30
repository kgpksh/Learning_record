def solution(food):
    
    tmp = []
    for i in range(1, len(food)):
        foodAmount = food[i] // 2
        for _ in range(foodAmount):
            tmp.append(str(i))
    
    return ''.join(tmp) + '0' + ''.join(list(reversed(tmp)))