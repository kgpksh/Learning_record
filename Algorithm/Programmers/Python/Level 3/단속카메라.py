def solution(routes):
    routes.sort(key = lambda x : (x[1], x[0]))
    end = routes[0][1]
    answer = 1
    for r in routes :
        s, e = r
        if s > end :
            answer += 1
            end = e
        
    return answer