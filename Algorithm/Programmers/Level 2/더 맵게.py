import heapq


def solution(s, k):
    h = []
    for i in s:
        heapq.heappush(h, i)
    answer = 0
    while True:
        small = heapq.heappop(h)
        big = heapq.heappop(h)
        bigger = small + 2 * big
        heapq.heappush(h, bigger)
        answer += 1
        check = heapq.heappop(h)

        if check >= k:
            break
        else:
            heapq.heappush(h, check)

        if len(h) == 1:
            return -1
    return answer
