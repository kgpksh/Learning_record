for _ in range(3):
    h1, m1, s1, h2, m2, s2=map(int,input().split())
    h=(h2-h1)*3600
    m=(m2-m1)*60
    s=(s2-s1)
    
    h3=(h+m+s)//3600
    m3=((h+m+s)-h3*3600)//60
    s3=(h+m+s)-h3*3600-m3*60
    print(str(h3)+' '+str(m3)+' '+str(s3))