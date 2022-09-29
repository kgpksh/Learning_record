from math import ceil
def solution(n, words):
    rec=[words[0]]
    dic=[i for i in range(n)]
    dic[0]=n
    for i in range(1,len(words)):
        if rec[i-1][-1]!=words[i][0] or words[i] in rec:
            tmp=(i+1)%n
            if tmp==0:
                repeat=(i+1)//n
            else:
                repeat=((i+1)//n)+1
            return [dic[tmp],repeat]
        else:
            rec.append(words[i])
    return [0,0]