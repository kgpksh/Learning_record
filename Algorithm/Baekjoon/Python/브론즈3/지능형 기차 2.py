people=0

top_people=0
for i in range(10):
    down,up=map(int,input().split())
    people=people+up-down
    top_people=max(people,top_people)
print(top_people)    