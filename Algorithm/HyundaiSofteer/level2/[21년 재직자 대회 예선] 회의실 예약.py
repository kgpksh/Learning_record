import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
rooms = []
for _ in range(n) :
    rooms.append(sys.stdin.readline().rstrip())

rooms.sort()

times = {}
answer = {}
for r in rooms :
    times[r] = [True] * 19
    answer[r] = []

for _ in range(m) :
    room, start, end = sys.stdin.readline().rstrip().split()
    for time in range(int(start), int(end)) :
        times[room][time] = False
        
def getAvailbleTime(schedule, start) :
    end = 0
    for t in range(start, len(schedule)) :
        if schedule[t] == False :
            break

        schedule[t] = False    
        end = t
    
    return end

def addZeroAtFront(n) :
    s = str(n)
    if len(s) == 2 :
        return s
    
    return '0' + s

for r in rooms :    
    for t in range(9, 18) :
        if times[r][t] :
            end = getAvailbleTime(times[r], t)
            answer[r].append(addZeroAtFront(t) + '-' + addZeroAtFront(min(end + 1, 18)))
            t = end

for r in rooms :
    print('Room ' + r + ':')
    if not answer[r] :
        print('Not available')
    
    else: 
        print(str(len(answer[r])) + ' available:')
        for t in answer[r] :
            print(t)

    if r != rooms[-1] :
        print('-----')