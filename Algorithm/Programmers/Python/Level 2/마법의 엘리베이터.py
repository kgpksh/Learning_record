def solution(storey):
    answer = 0
    strNums = list(map(int, reversed(str(storey))))
    strNums.append(0)
    
    for idx in range(len(strNums) - 1) :
        if 10 - strNums[idx] + nearer(strNums[idx + 1] + 1) <= strNums[idx] + nearer(strNums[idx + 1]) :
            answer += 10 - strNums[idx]
            strNums[idx + 1] += 1
            continue
        
        answer += strNums[idx]
        
    return answer + strNums[-1]

def nearer(num) :
    if num > 5 :
        return 10 - num
    
    return num