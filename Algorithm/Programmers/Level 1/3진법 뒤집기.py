def solution(n):
    answer = 0
    s = get(n)
    for i in range(len(s)):
        answer += int(s[i]) * (3**i)
    return answer


def get(n):
    s = ""
    while True:
        if n < 3:
            s = str(n) + s
            break
        else:
            s = str(n % 3) + s
            n = n // 3
    return s
