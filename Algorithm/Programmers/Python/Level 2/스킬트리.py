def solution(skill, skill_trees):
    order = set(skill)
    answer = 0
    
    for tree in skill_trees :
        non_tree = set(tree) - order
        
        for n in non_tree :
            tree = tree.replace(n, '')
            
        if skill.startswith(tree) :
            answer += 1
    return answer