from itertools import combinations as c
def solution(number):
    answer = 0
    for i in c(number,3):
        if sum(i) == 0:
            answer+=1
    return answer