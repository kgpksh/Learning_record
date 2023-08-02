def solution() :
    changing = input()
    if changing == '1 2 3 4 5 6 7 8' :
        return 'ascending'
    
    if changing == '8 7 6 5 4 3 2 1' :
        return 'descending'
    
    return 'mixed'

print(solution())