import sys
T = int(sys.stdin.readline().rstrip())
chars = {'-' : 0b0000000, '0' : 0b1110111, '1' : 0b0010010, '2' : 0b1011101, '3' : 0b1011011, '4' : 0b0111010, '5' : 0b1101011,
            '6' : 0b1101111, '7' : 0b1110010, '8' : 0b1111111, '9' : 0b1111011}

def countOne(n) :
    count = 0
    while n:
        n &= (n-1)
        count += 1
    return count

def solution() :
    a, b = map(str, sys.stdin.readline().rstrip().split())
    a = '-' * (5 - len(a)) + a
    b = '-' * (5 - len(b)) + b

    answer = 0

    for idx in range(5) :
        A = a[idx]
        B = b[idx]
        answer += countOne(chars[A] ^ chars[B])

    print(answer)

for _ in range(T) :
    solution()