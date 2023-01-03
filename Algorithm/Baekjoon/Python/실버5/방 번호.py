from math import ceil
number = input()

count = {'0':0}
sixnine = 0
for n in number:
    if n == '6' or n == '9':
        sixnine +=1
    else :
        count[n] = count.get(n, 0) + 1
six = ceil(sixnine / 2)
print(max(max(count.values()), six))