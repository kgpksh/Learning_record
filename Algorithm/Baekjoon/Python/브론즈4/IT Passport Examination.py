tc=int(input())

for _ in range(tc):
    n,a,b,c=map(int,input().split())
    d=a+b+c
    if a>=10.5 and b>=7.5 and c>=12 and d>=55:
        print(str(n)+' '+str(d)+' PASS')
    else:
        print(str(n)+' '+str(d)+' FAIL')