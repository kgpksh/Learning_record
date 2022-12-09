k, d, a = map(int, input().split("/"))

def answer(k,d,a):
    if d == 0:
        return 'hasu'
    
    if k+a < d:
        return 'hasu'
    
    return 'gosu'

print(answer(k,d,a))