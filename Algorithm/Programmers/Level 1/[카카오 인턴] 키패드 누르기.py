def solution(numbers, hand):
    lft = {1: [1, 1], 4: [1, 2], 7: [1, 3]}
    rit = {3: [3, 1], 6: [3, 2], 9: [3, 3]}
    middle = {2: [2, 1], 5: [2, 2], 8: [2, 3], 0: [2, 4]}
    lp = [1, 4]
    rp = [3, 4]
    answer = ""
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            lp = lft[i]
        elif i in [3, 6, 9]:
            answer += "R"
            rp = rit[i]
        else:
            x, y = middle[i]
            lx, ly = lp
            rx, ry = rp
            ld = abs(lx - x) + abs(ly - y)
            rd = abs(rx - x) + abs(ry - y)
            use = hand[0].upper()
            if ld == rd:
                answer += use
                if use == "R":
                    rp = middle[i]
                else:
                    lp = middle[i]
            elif ld < rd:
                answer += "L"
                lp = middle[i]
            else:
                answer += "R"
                rp = middle[i]

    return answer
