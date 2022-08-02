n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[1], x[0]))
for i in lst:
    print(str(i[0]) + " " + str(i[1]))
