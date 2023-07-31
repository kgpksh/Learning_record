from collections import deque
def solution(m, musicinfos):
    dic = {'C#' : 'c', 'D#' : 'd', 'F#' : 'f', 'G#' : 'g', 'A#' : 'a'}
    for d in dic :
        m = m.replace(d, dic[d])
        
    answer = []
    musics = makeList(musicinfos)
    
    idx = 0
    for singleMusic in musics :
        time, name, music = singleMusic
        music = musicEdit(music, dic, time)
        
        if music.find(m) != -1 :
            answer.append((idx, time, name))
    
    answer = sorted(answer, key = lambda x : (-x[1], x[0]))
    
    if answer :
        return answer[0][2]
    
    return '(None)'

def makeList(musicinfos) :
    result = []
    for m in musicinfos :
        start, end, name, music = m.split(',')
        result.append((diffMinutes(start, end), name, music))
    return result

def diffMinutes(start, end) :
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    
    return eh * 60 + em - sh * 60 - sm

def musicEdit (music, dic, L) :
    result = []
    
    for d in dic :
        music = music.replace(d, dic[d])
    
    music = deque(music)
    
    for _ in range(L) :
        result.append(music[0])
        music.rotate(-1)
    return ''.join(result)