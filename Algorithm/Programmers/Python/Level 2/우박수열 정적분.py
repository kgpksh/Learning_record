def solution(k, ranges):
    answer = []
    count = 0
    arr = []
    while k != 1 :
        arr.append(k)
        if k % 2 == 1 :
            k = k * 3 + 1
        else :
            k //= 2
            
        count += 1
    arr.append(1)
    
    for r in ranges :
        a, b = r
        b = count + b
        if a > b :
            answer.append(-1)
            continue
        result = 0
        for x in range(a, b) :
            small = min(arr[x], arr[x + 1])
            big = max(arr[x], arr[x + 1])
            result += small + (big - small) / 2
        answer.append(result)
    return answer