def solution(s):
    maxLen = len(s)
    answer = maxLen
    for i in range(1, int(len(s)/2) + 1) :
        pos = 0
        length = maxLen
        
        while pos + i <= maxLen :
            unit = s[pos : pos + i]
            pos += i
            cnt = 0
            while pos + i <= maxLen :
                if unit == s[pos : pos + i] :
                    cnt += 1
                    pos += i
                    continue
                break
                
            if cnt > 0 :
                length -= cnt * i

                if cnt < 9 :
                    length += 1
                elif cnt < 99 :
                    length += 2
                elif cnt < 999 :
                    length += 3
                else :
                    length += 4
                    
            answer = min(answer, length)
    return answer