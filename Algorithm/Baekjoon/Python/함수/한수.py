i = input()
cnt = 0
for a in range(1, int(i) + 1):
    if a < 100:
        cnt += 1

    elif a == 1000:
        pass

    else:
        tmp = str(a)
        if int(tmp[0]) - int(tmp[1]) == int(tmp[1]) - int(tmp[2]):
            cnt += 1
print(cnt)
