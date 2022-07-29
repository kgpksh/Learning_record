import sys

n = input()

answer = 0
for i in sys.stdin.readline().rstrip():
    answer += int(i)

print(answer)
