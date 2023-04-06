from math import ceil
def solution(fees, records):
    answer = []
    cumulated = {}
    timeRecord = {}
    
    for rec in records :
        time, num, io = rec.split()
        tmp = timeRecord.get(num, [])
        tmp.append(time)
        timeRecord[num] = tmp
        
    for tr in timeRecord :
        if len(timeRecord[tr]) % 2 == 1 :
            tmp = timeRecord[tr]
            tmp.append('23:59')
            timeRecord[tr] = tmp
        for cut in range(0, len(timeRecord[tr]) - 1, 2) :
            diff = diffMin(timeRecord[tr][cut], timeRecord[tr][cut + 1])
            cumulated[tr] = cumulated.get(tr, 0) + diff
            
    for time in cumulated :
        cumulated[time] = calculateFees(fees, cumulated[time])
        
    cumulated = sorted(cumulated.items(), key = lambda x : x[0])
    for c in cumulated :
        answer.append(c[1])
    return answer

def calculateFees(fees, minutes) :
    basicTime, basicFee, additionalTime, additionalFee = fees
    return basicFee + ceil(max(minutes - basicTime, 0) / additionalTime) * additionalFee

def diffMin(IN, OUT) :
    h1, m1 = map(int, IN.split(':'))
    h2, m2 = map(int, OUT.split(':'))
    
    return (h2 * 60 + m2) - (h1 * 60 + m1)