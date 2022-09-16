dic={'a':True,'e':True,'i':True,'o':True,'u':True,'A':True,'E':True,'I':True,'O':True,'U':True}
while True:
    string=input()
    if string=='#':
        break
    answer=0
    for s in string:
        if dic.get(s,False):
            answer+=1
    print(answer)