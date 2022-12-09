n,m = map(int, input().split())

def answer(n,m) :
    newbie = [1,2]
    if n in newbie :
        return "NEWBIE!"
    
    if n <= m :
        return "OLDBIE!"
    
    return "TLE!"

print(answer(m,n))