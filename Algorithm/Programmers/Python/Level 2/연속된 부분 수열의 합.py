def solution(sequence, k):
    answer = []
    start, end = 0, 0
    L = len(sequence)
    currentSum = sequence[0]
    while start != L :
        if currentSum > k :
            currentSum -= sequence[start]
            start += 1
            continue
            
        if currentSum == k :
            answer.append([start, end])
            
        if end == L - 1 :
            break
        end += 1
        currentSum += sequence[end]
    
    answer = sorted(answer, key = lambda x : (x[1] - x[0], x[0]))
    return answer[0]