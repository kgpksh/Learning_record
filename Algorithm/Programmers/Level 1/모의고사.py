def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    tmp = [0, 0, 0]
    answer = []
    for i in range(0, len(answers)):
        if answers[i] == a[i % 5]:
            tmp[0] += 1

        if answers[i] == b[i % 8]:
            tmp[1] += 1

        if answers[i] == c[i % 10]:
            tmp[2] += 1

    m = max(tmp)

    for i in range(3):
        if tmp[i] == m:
            answer.append(i + 1)
    return answer
