import sys
N = int(sys.stdin.readline().strip())
def isPrime(n) :
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    return True

def solve(n) :
    while True :
        if isPrime(n) :
            return n
        n += 1
for _ in range(N) :
    n = int(sys.stdin.readline().strip())
    if n < 3 :
        print(2)
        continue
    print(solve(n))