# 원순열 전체를 다룰때는 같은 배열 2개를 이어붙이자

def solution(elements):
    answer = set()
    arr = elements + elements
    length = len(elements)
    
    for i in range(1, length + 1) :
        seed = sum(arr[: i])
        answer.add(seed)
        
        for j in range(i, length + i - 1):
            seed = seed -arr[j - i] + arr[j]
            answer.add(seed)
            
    return len(answer)