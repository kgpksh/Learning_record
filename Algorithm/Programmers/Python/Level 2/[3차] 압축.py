from collections import deque
def solution(msg):
    answer = []
    last = 26
    dic = {}
    for i in range(ord('A'), ord('Z') + 1) :
        idx = i - ord('A') + 1
        dic[chr(i)] = idx
    
    msg = deque(msg)
    dq = deque([msg.popleft()])
    
    while dq :
        while msg and dic.get(''.join(dq) + msg[0], 0) > 0 :
            dq.append(msg.popleft())
            
        word = ''.join(dq)
        answer.append(dic[word])
        
        if msg :
            last += 1
            dic[word + msg[0]] = last

        dq.clear()

        if msg :
            dq.append(msg.popleft())
                
    return answer