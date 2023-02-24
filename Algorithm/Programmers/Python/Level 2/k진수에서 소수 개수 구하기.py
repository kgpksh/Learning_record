def solution(n, k):
    answer = 0
    
    nums = convert(n, k)
    while '00' in nums :
        nums = nums.replace('00', '0')
        
    nums = nums.split('0')
    while '' in nums :
        nums.remove('')
        
    for num in nums :
        if isPrime(int(num)) :
            answer += 1
    
    return answer

def isPrime(n) :
    if n == 1 :
        return False
    for i in range(2, int(n**0.5) + 1) :
        if n%i == 0:
            return False
        
    return True

def convert(n, k) :
    result = []
    
    while n != 0 :
        result.append(str(n%k))
        n //= k
        
    return ''.join(reversed(result))