import heapq

def solution(operations):
    answer = []
    min_heap_direction = True
    for o in operations :
        if o[0] == 'I' :
            if min_heap_direction :
                heapq.heappush(answer, int(o.split()[1]))
            else :
                heapq.heappush(answer, -int(o.split()[1]))
            continue
        
        if o[2] == '-' :
            if not answer :
                continue
            if not min_heap_direction :
                answer = list(map(lambda e : -e, answer))
                heapq.heapify(answer)
                min_heap_direction = True
            heapq.heappop(answer)
            continue
        
        if not answer :
            continue
        if min_heap_direction :
            answer = list(map(lambda e : -e, answer))
            heapq.heapify(answer)
            min_heap_direction = False
        heapq.heappop(answer)
    
    if not answer :
        return [0, 0]
    answer.sort()
    return [answer[-1], answer[0]]