def solution(sizes):
    q = [0, 0]
    for i in sizes:
        i.sort()
    for i in sizes:
        for j in range(2):
            if q[j] < i[j]:
                q[j] = i[j]
    return q[0] * q[1]
