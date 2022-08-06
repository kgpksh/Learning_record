def fac(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


f = "".join(reversed(str(fac(int(input())))))
answer = 0
for i in f:
    if i == "0":
        answer += 1
    else:
        break
print(answer)
