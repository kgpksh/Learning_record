all=set([i for i in range(1,31)])
students=set()
for _ in range(28):
    students.add(int(input()))
print(min(list(all-students)))
print(max(list(all-students)))