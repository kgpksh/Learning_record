print('Gnomes:')
tc=int(input())
for _ in range(tc):
    arr=list(map(int,input().split()))
    if arr==sorted(arr) or arr==sorted(arr,reverse=True):
        print('Ordered')
    else:
        print('Unordered')