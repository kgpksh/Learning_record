import sys

N = int(sys.stdin.readline().strip())
record = {}
for _ in range(N) :
    name, state = sys.stdin.readline().strip().split()
    
    if record.get(name, False) :
        del record[name]
        continue
    record[name] = True
    
for name in sorted(record, reverse = True) :
    print(name)