def solution(begin, target, words):
    if not target in words:
        return 0
    
    global size
    global answer
    global word_len
    word_len = len(words[0])
    answer = 0
    size = len(words)
    visited = [False] * size
    
    dfs(begin, target, words, 0, visited)
    
    return answer
    

def dfs(now, target, words, step, visited):
    if now == target:
        global answer
        if answer == 0:
            answer = step
        else:
            answer = min(answer, step)
    
    for w in range(size):
        if finder(words[w], now) and visited[w] == False:
            visited[w] = True
            dfs(words[w], target, words, step + 1, visited)
            visited[w] = False
            
def finder(new, old):
    cnt = 0
    for i in range(word_len):
        if new[i] != old[i]:
            cnt +=1
    return cnt == 1