n = int(input())
init = 666
cnt = 1
while True:
    if cnt == n:
        print(init)
        break

    init += 1
    if "666" in str(init):
        cnt += 1
