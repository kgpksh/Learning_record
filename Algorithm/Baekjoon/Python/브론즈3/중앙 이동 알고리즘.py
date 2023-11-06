N = int(input())

L = 2
for _ in range(N) :
    L += L - 1
    
print(L ** 2)