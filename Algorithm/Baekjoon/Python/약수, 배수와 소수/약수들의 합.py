while True :
    n = int(input())
    
    if n == -1 :
        break
        
    tmp = set()
    tmp.add(1)
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            tmp.add(i)
            tmp.add(n // i)
            
    if sum(tmp) == n :
        tmp = sorted(list(tmp))
        tmp2 = list(map(str, tmp))
        print(str(n) + ' = ' + ' + '.join(tmp2))
    else :
        print(str(n) + ' is NOT perfect.')