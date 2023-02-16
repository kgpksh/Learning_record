from itertools import product
def solution(word):
    lst = ['A', 'E', 'I', 'O', 'U']
    all_product = []
    
    for i in range(1, 6):
        all_product += list(product(lst, repeat = i))
    all_product.sort()
    
    for p in range(len(all_product)) :
        if ''.join(all_product[p]) == word :
            return p + 1