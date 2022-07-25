def solution(arr, divisor):
    tmp = []
    for i in arr:
        if i % divisor == 0:
            tmp.append(i)
    if not tmp:
        return [-1]
    else:
        return sorted(tmp)
