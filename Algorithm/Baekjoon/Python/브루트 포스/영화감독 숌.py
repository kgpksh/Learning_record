n = int(input())
init = 666
cnt = 1
while cnt < n:
    init += 1
    for i in range(len(str(init)), 2, -1):
        if "6" * i in str(init):
            cnt += 1
            break
print(init)
