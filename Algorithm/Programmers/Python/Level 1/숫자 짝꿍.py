def solution(X, Y):
    dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    answer = []
    
    for x in X:
        dic[x] = dic[x] + 1
    
    for y in Y:
        if dic[y] > 0:
            answer.append(y)
        dic[y] = dic[y] - 1
        
    answer.sort(reverse = True)
    
    result = ''.join(answer)
    if result == '':
        return '-1'
    
    if result[0] == '0':
        return '0'
    
    return result