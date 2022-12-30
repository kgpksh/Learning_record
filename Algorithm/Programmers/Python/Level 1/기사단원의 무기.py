def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        y = yaksu(i)
        if y > limit:
            answer += power
        else:
            answer += y
    return answer


def yaksu(n):
    if n == 1:
        return 1
    sqrt = int(n**0.5)
    
    answer = 0
    