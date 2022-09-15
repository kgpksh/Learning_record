tc=int(input())
for _ in range(tc):
    x1,y1,r1,x2,y2,r2=map(int,input().split(" "))
    distance=(x2-x1)**2+(y2-y1)**2
    if x1==x2 and y1==y2:
        if r1==0 and r2==0:
            print(1)
        # 완전히 겹치는 경우
        elif r1==r2:
            print(-1)
        # 겹치지 않는 경우
        else:
            print(0)
    else:
        #외접하는 경우와 내접하는 경우
        if distance==(r1+r2)**2  or distance==(r2-r1)**2:
            print(1)
        # 한 원이 다른 원 안에 들어있고, 내접하지 않을때
        elif distance<(r2-r1)**2:
            print(0)
        #중점간의 거리가 반경합보다 작아 교점 2개
        elif distance<(r1+r2)**2:
            print(2)
        # 나머지
        else:
            print(0)