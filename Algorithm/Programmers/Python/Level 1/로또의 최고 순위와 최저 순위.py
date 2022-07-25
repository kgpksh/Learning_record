def grade(n):
    if n == 0:
        return 6
    else:
        return 7 - n


def solution(lottos, win_nums):
    answer = []
    zeros = 0

    _lottos = set(lottos)
    _win_nums = set(win_nums)
    number = 6 - len(_win_nums - _lottos)

    for i in range(len(lottos)):
        if lottos[i] == 0:
            zeros += 1

    answer.append(grade(number + zeros))
    answer.append(grade(number))
    return answer
