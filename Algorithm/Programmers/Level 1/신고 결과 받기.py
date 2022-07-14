def solution(id_list, report, k):
    _report = {}
    s = set(report)
    for i in s:
        a, b = i.split()
        tmp = _report.get(b, [])
        tmp.append(a)
        _report[b] = tmp
    lst = {}

    for i in id_list:
        lst[i] = 0

    for i in _report:
        if len(_report[i]) >= k:
            for b in _report[i]:
                lst[b] += 1
    return list(lst.values())
