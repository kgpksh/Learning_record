def solution(arr):
    global answer, square
    answer, square = [0, 0], arr
    maxi = len(arr)
    crack(0, maxi, 0, maxi)
    return answer

def crack(miniY, maxiY, miniX, maxiX) :
    global answer
    tmp = [cut[miniX: maxiX] for cut in square[miniY : maxiY]]
    check = count(tmp, maxiY - miniY)
    if check != -1 :
        answer[check] += 1
        return
    
    crack(miniY, (miniY + maxiY) // 2, miniX, (miniX + maxiX) // 2)
    crack((miniY + maxiY) // 2, maxiY, miniX, (miniX + maxiX) // 2)
    crack(miniY, (miniY + maxiY) // 2, (miniX + maxiX) // 2, maxiX)
    crack((miniY + maxiY) // 2, maxiY, (miniX + maxiX) // 2, maxiX)
        
        
def count(square, size) :
    if len(set(square[0])) != 1:
        return -1
    for i in range(1, size) :
        if square[i] != square[0] :
            return -1
        
    return square[0][0]