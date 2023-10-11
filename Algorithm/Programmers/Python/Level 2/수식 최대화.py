from itertools import permutations
def solution(expression):
    answer = 0
    for p in permutations(['+', '-', '*'], 3) :
        answer = max(answer, abs(calculate(p, expression, 0)))
    
    return answer

def calculate(order, exp, depth) :
    if order[depth] == '*' :
        result = 1
        for e in exp.split('*') :
            if depth == 2 :
                result *= int(e)
            else :
                result *= calculate(order, e, depth + 1)
        return result
    
    if order[depth] == '+' :
        result = 0
        for e in exp.split('+') :
            if depth == 2 :
                result += int(e)
            else :
                result += calculate(order, e, depth + 1)
        return result
    
    if order[depth] == '-' :
        splt = exp.split('-')
        if depth == 2 :
            result = int(splt[0])
        else :
            result = calculate(order, splt[0], depth + 1)
            
        for e in range(1, len(splt)) :
            if depth == 2 :
                result -= int(splt[e])
            else :
                result -= calculate(order, splt[e], depth + 1)
        return result