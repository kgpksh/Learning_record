def solution(s):
    s = s[2:-2]
    lst = s.split("},{")

    lst.sort(key=len)

    answer = []
    lst2 = []

    for i in lst:
        lst2.append(i.split(","))
    fs = set(lst2[0])

    answer.append(int(lst2[0][0]))

    for i in lst2:
        bs = set(i)
        for j in bs - fs:
            answer.append(int(j))
        fs = bs

    return answer
