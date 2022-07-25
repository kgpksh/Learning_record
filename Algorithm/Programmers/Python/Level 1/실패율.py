def solution(N, stages):
    dic = {}
    for i in range(N + 1):
        dic[i + 1] = 0
    for i in stages:
        dic[i] += 1
    lst = []
    answer = []
    users = len(stages)

    for i in range(N):
        if users != 0:
            ratio = dic[i + 1] / users
            lst.append([ratio, i + 1])
            users -= dic[i + 1]
        else:
            lst.append([0, i + 1])

    sol = sorted(lst, key=lambda x: (-x[0], x[1]))
    for i in sol:
        answer.append(i[1])
    return answer
