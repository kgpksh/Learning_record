def solution(s):
    answer = True
    if len(s) != 4:
        return False
    for i in s:
        if i.isalpha():
            answer = False
            break
    return answer
