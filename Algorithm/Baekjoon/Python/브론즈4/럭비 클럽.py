while True:
    name=input()
    if name=='# 0 0':
        break
    
    a,b,c=map(str,name.split())
    if int(b)>17 or int(c)>=80:
        print(a+' Senior')
    else:
        print(a+' Junior')