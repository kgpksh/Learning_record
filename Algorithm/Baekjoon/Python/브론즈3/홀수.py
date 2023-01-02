big = 0
odd = 100

for _ in range(7):
    i = int(input())
    
    if i%2 !=0:
        odd = min(odd, i)
        big += i

if odd ==100 :
    print(-1)
else:
    print(big)
    print(odd)