while True:
    n=input()
    if n=='0':
        break
    answer=0
    l=len(n)
    answer+=l+1
    
    one=n.count('1')
    answer+=one*2
    l-=one
    
    zero=n.count('0')
    answer+=zero*4
    l-=zero
    
    answer+=l*3
    print(answer)