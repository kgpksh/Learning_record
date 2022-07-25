def solution(arr):
    answer = []
    idx = arr.index(min(arr))
    a = arr[:idx] + arr[idx + 1 :]
    if not a:
        return [-1]
    else:
        return a
