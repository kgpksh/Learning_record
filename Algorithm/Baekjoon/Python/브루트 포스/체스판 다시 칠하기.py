import math

n, m = map(int, input().split(" "))

sample = ["WBWBWBWB", "BWBWBWBW"]
board = []
for i in range(n):
    board.append(input())

answer = math.inf
for i in range(n - 7):
    tmp = board[i : i + 8]
    for j in range(m - 7):
        for c in range(2):
            cnt = 0
            for t in range(8):
                tmp2 = tmp[t][j : j + 8]
                if (t + c) % 2 == 0:
                    correct = sample[0]
                else:
                    correct = sample[1]

                for check in range(8):
                    if correct[check] != tmp2[check]:
                        cnt += 1
            answer = min(answer, cnt)

print(answer)
