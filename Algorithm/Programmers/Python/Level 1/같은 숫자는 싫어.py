from collections import Counter


def solution(arr):
    check = arr[0]
    answer = [check]
    for i in range(1, len(arr)):
        if arr[i] != check:
            answer.append(arr[i])
            check = arr[i]
    return answer
