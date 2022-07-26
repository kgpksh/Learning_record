n = int(input())

for i in range(n):
    result = input()

    score = 0
    adder = 0
    for r in result:
        if r == "O":
            adder += 1
            score += adder
        else:
            adder = 0
    print(score)
