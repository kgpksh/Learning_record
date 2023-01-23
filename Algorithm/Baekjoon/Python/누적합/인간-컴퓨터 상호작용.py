string = input()
numberOfQuestion = int(input())

for _ in range(numberOfQuestion):
    a, l, r = map(str, input().split())
    
    sliced = string[int(l) : int(r) + 1]
    print(sliced.count(a))