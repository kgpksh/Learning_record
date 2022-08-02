import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
num = {}
name = {}
for i in range(1, m + 1):
    pok = sys.stdin.readline().rstrip()
    num[i] = pok
    name[pok] = i

for i in range(n):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(num[int(question)])
    else:
        print(name[question])
