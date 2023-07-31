def solution(n):
    global answer
    answer = 0
    for x in range(n) :
        queens = [x]
        dfs(queens, 1, 1, n)
    return answer

def dfs(queens, Y, depth, n) :
    if depth == n :
        global answer
        answer += 1
        return
    
    for x in range(n) :
        if not canAttack(queens, (Y, x)) :
            queens.append(x)
            dfs(queens, Y + 1, depth + 1, n)
            
            if queens :
                queens.pop()


def canAttack(queens, added) :
    for y, x in enumerate(queens) :
        Y, X = added
        if x == X or abs((x - X) / (y - Y)) == 1 :
            return True
        
    return False