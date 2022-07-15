from collections import Counter


def solution(str1, str2):

    s1 = str1.lower()
    s2 = str2.lower()
    print(s1)
    print(s2)

    lst1 = cut(s1)
    lst2 = cut(s2)

    dic1 = Counter(lst1)
    dic2 = Counter(lst2)

    andlist = set(lst1) & set(lst2)

    ss1 = set(lst1) - set(lst2)
    ss2 = set(lst2) - set(lst1)

    intersection = 0
    merge = 0
    for i in andlist:
        intersection += min(dic1[i], dic2[i])
        merge += max(dic1[i], dic2[i])

    for i in ss1:
        merge += dic1[i]
    for i in ss2:
        merge += dic2[i]

    if merge != 0:
        answer = int(intersection * 65536 / merge)
    else:
        answer = 65536
    return answer


def cut(s):
    lst = []
    for i in range(len(s) - 1):
        if s[i : i + 2].isalpha():
            lst.append(s[i : i + 2])
    return lst
