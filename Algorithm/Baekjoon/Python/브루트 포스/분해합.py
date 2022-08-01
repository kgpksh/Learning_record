n = input()
answer = 0
for i in range(1, int(n)):
    s = str(i)
    num = i
    for j in s:
        num += int(j)
    if num == int(n):
        answer = i
        break
print(answer)
