from bisect import bisect_right as br
def solution(book_time):
    starts, ends = timeToNum(book_time)
    answer = 0
    
    for s in starts :
        binarySearched = br(ends, s)
        if binarySearched == 0 :
            answer += 1
            continue
        del ends[binarySearched - 1]
            
    return answer

def timeToNum(book_time) :
    starts, ends = [], []
    for start, end in book_time :
        startHour, startMin = map(int, start.split(':'))
        endHour, endMin = map(int, end.split(':'))
        
        startTime = startHour * 60 + startMin
        endTime = endHour * 60 + endMin + 10
        
        starts.append(startTime)
        ends.append(endTime)
        
    return starts, sorted(ends)