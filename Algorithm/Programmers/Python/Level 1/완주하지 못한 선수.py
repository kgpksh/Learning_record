def solution(participant, completion):
    dic = {}
    sumhash = 0
    for i in participant:
        dic[hash(i)] = i
        sumhash += hash(i)

    for i in completion:
        sumhash -= hash(i)

    return dic[sumhash]
