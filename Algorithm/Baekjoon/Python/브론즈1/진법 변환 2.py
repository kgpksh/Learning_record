N, B = map(int, input().split())
dic = {}
for i in range(11) :
    dic[i] = str(i)
for i in range(10, 36) :
    alphabet = chr(ord('A') + i - 10)
    dic[i] = alphabet

answer = []

while N > 0 :
    answer.append(dic[N % B])
    N //= B
print(''.join(reversed(answer)))