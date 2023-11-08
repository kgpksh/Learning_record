import sys

while True :
    triangle = sys.stdin.readline().strip()
    if triangle == '0 0 0' :
        break
    
    triangle = list(map(int,triangle.split()))
    triangle.sort()
    
    if triangle[0] + triangle[1] <= triangle[2] :
        print("Invalid")
        continue
    
    types = len(set(triangle))
    
    if types == 1 :
        print("Equilateral")
        continue
        
    if types == 2 :
        print("Isosceles")
        continue
        
    print("Scalene")