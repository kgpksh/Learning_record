def solution(arr1, arr2):    
    size = len(arr1[0])
    answer = []
    
    for y in range(len(arr1)) :
        tmp = []
        for x in range(len(arr2[0])) :
            tmp.append(singleCalculate(arr1, arr2, y, x, size))
        
        answer.append(tmp)
    return answer

def singleCalculate(arr1, arr2, Y, X, L) :
    result = 0
    for element in range(L) :
        result += arr2[element][X] * arr1[Y][element]
            
    return result