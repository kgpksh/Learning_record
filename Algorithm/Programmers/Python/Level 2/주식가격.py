def solution(prices):
    l = len(prices)
    answer = [0] * l
    for i in range(l):
        for j in range(i + 1, l):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer
