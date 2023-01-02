tc = int(input())

converter = {'kg' : 2.2046, 'lb' : 0.4536, 'l' : 0.2642, 'g' : 	3.7854}
english = {'kg' : 'lb', 'lb' : 'kg', 'l' : 'g', 'g' : 'l'}

for _ in range(tc):
    num, eng = map(str, input().split(' '))
    
    n = converter[eng] * float(num)
    e = english[eng]
    print(format(n, '.4f') + ' ' + e)