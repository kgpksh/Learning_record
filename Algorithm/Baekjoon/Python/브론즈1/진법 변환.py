N, B = input().split()
B = int(B)
dic = {}
for i in range(11) :
    dic[str(i)] = i
for i in range(10, 36) :
    alphabet = chr(ord('A') + i - 10)
    dic[alphabet] = i

answer = 0
count = 0
for s in reversed(N) :
    answer += dic[s] * (B ** count)
    count += 1
    
print(answer)