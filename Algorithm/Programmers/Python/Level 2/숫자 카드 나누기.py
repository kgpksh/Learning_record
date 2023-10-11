from math import gcd
def solution(arrayA, arrayB):
    A = arrayA[0]
    B = arrayB[0]
    for a in arrayA :
        A = gcd(A, a)
    for b in arrayB :
        B = gcd(B, b)
        
    for a in arrayA :
        if a % B == 0 :
            B = 0
            break
    
    for b in arrayB :
        if b % A == 0 :
            A = 0
            break
            
    return max(A, B)