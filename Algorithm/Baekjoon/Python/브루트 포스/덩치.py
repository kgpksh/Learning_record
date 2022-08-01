case = int(input())
lst = []
for i in range(case):
    lst.append(list(map(int, input().split())))

ranking = []
for i in lst:
    rank = 0
    for j in lst:
        if j[0] > i[0] and j[1] > i[1]:
            rank += 1
    ranking.append(rank)

answer = ""
for s in ranking:
    answer = answer + str(s + 1) + " "
print(answer[:-1])
