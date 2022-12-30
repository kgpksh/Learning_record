def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        d = dic.get(s[i], -1)
        answer.append(check(d, i))
        dic[s[i]] = i
    
    return answer

def check(d, index):
    if d == -1:
        return -1
    return index - d