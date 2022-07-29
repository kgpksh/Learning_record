tc = int(input())

for i in range(tc):
    n, s = map(str, input().split(" "))
    for j in s:
        print(j * int(n), end="")
    print()
