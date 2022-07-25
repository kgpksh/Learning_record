def solution(n):
    answer = ""
    n = n.lower()
    for i in n:
        if i.isdigit() or i.isalpha() or i in ["-", "_", "."]:
            answer += i

    while ".." in answer:
        answer = answer.replace("..", ".")

    if answer and answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]

    if len(answer) == 0:
        answer = "a"

    if len(answer) > 15:
        answer = answer[:15]

        if answer[-1] == ".":
            answer = answer[:-1]

    while len(answer) < 3:
        answer += answer[-1]

    return answer
