def solution(n):
    answer = 0

    save = [True] * (n + 1)
    save[0:2] = False, False

    for i in range(2, n + 1):
        if save[i]:
            answer += 1
            for j in range(2 * i, n + 1, i):
                save[j] = False
    return answer
