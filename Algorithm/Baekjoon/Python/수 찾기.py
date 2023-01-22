def binarySearch(array, target, start, end):
    while start<=end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return 1
        
        if array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
            
    return 0


N = input()
array = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

array.sort()
L = len(array)
for t in targets:
    print(binarySearch(array, t, 0, L - 1))