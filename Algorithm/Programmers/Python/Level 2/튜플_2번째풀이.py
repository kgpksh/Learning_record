def solution(s):
    array = s[2 : len(s) - 2].split('},{')
    array = sorted(array, key = lambda x : len(x))
    dic = {}
    for arr in array[-1].split(',') :
        dic[int(arr)] = True
    
    answer = []
    for arr in array :
        for element in map(int, arr.split(',')) :
            if dic[element] :
                answer.append(element)
                dic[element] = False
                continue
    return answer