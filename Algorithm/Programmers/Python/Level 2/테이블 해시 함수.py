def solution(data, col, row_begin, row_end):
    sdata = sorted(data, key = lambda x : (x[col - 1], -x[0]))
    
    answer = get_SI(sdata[row_begin - 1], row_begin)
    
    for idx in range(row_begin + 1, row_end + 1) :
        answer ^= get_SI(sdata[idx - 1], idx)
    
    return answer

def get_SI(tup, idx) :
    result = 0
    for t in tup :
        result += t % idx
    return result