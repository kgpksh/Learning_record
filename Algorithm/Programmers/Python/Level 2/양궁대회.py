def solution(n, info):
    global appeach_list
    appeach_list = info
    
    global largest_gap
    global available_list
    largest_gap = 0
    available_list = []
    dfs(n, 10, [])
    
    if largest_gap == 0 :
        return [-1]
    
    reversed_elements = list(map(lambda element : list(reversed(element)), available_list))
    reversed_elements.sort(reverse = True)
    return list(reversed(reversed_elements[0]))

def dfs(arrows, point, record) :
    if point == 0 :
        lion_list = record + [arrows]
        gap = get_score_gap(lion_list)
        
        global largest_gap
        global available_list
        if gap > largest_gap :
            available_list.clear()
            largest_gap = gap
            available_list.append(lion_list)
        elif gap == largest_gap :
            available_list.append(lion_list)
        return
    
    for current_arrow in range(arrows, -1, -1) :
        dfs(arrows - current_arrow, point - 1, record + [current_arrow])
        
def get_score_gap(lion_list) :
    appeach, lion = 0, 0
    for score in range(10, -1, -1) :
        idx = 10 - score
        if appeach_list[idx] == 0 and lion_list[idx] == 0 :
            continue
            
        if appeach_list[idx] < lion_list[idx] :
            lion += score
        else :
            appeach += score
    return lion - appeach