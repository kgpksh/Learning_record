ham=[]
bev=[]
for _ in range(3):
    ham.append(int(input()))
for _ in range(2):
    bev.append(int(input()))
    
print(min(ham)+min(bev)-50)