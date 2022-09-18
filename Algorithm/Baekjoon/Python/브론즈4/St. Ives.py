while True:
    n=float(input())
    if n==0:
        break
    answer=0
    for i in range(5):
        answer+=n**i
    
    print('{:.2f}'.format(answer))