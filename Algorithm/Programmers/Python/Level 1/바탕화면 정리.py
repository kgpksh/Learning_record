def solution(wallpaper):
    answer = [50, 50, 0, 0]
    for h in range(len(wallpaper)) :
        for w in range(len(wallpaper[0])) :
            if wallpaper[h][w] == '#' :
                answer[0] = min(answer[0], h)
                answer[1] = min(answer[1], w)
                answer[2] = max(answer[2], h)
                answer[3] = max(answer[3], w)
    answer[2] += 1
    answer[3] += 1
    return answer