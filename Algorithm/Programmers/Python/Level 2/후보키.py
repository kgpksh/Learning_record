from itertools import combinations
def solution(relation):
    global relations
    relations = relation
    row_len = len(relation[0])
    global keys, c
    keys = []
    tuples = []
    for r in range(1, row_len + 1) :
        tuples += list(combinations([i for i in range(row_len)], r))
    
    answer = 0
    for tup in tuples :
        if not isMinimum(tup) :
            continue
            
        if isUnique(tup) :
            answer += 1
        
    return answer

def isMinimum(tup) :
    set_tup = set(tup)
    
    for key in keys :
        if set(key).issubset(set_tup) :
            return False
        
    return True

def isUnique(tup) :
    tmp_rec = {}
    for r in relations :
        query = []
        for t in tup :
            query.append(r[t])
            
        tmp_data = ''.join(query)
        isExists = tmp_rec.get(tmp_data, False)
        if isExists :
            return False
        tmp_rec[tmp_data] = True
        
    keys.append(set(tup))
    return True