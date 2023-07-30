def solution(weights):
    answer = 0
    
    counter = {}
    table = {}
    distances = (2, 3, 4)
    
    for w in weights :
        for d in distances :
            torque = w * d            
            answer += table.get(torque, 0) - counter.get(w, 0)
            table[torque] = table.get(torque, 0) + 1
        
        answer += counter.get(w, 0)
        counter[w] = counter.get(w, 0) + 1
            
    return answer