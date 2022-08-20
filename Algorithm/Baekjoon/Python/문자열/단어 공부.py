from collections import Counter
import sys

s = sys.stdin.readline().upper()
cc = sorted(Counter(s).items(), key=lambda x: -x[1])
print(cc)
l = len(cc)
if l > 2:
    if cc[0][1] == cc[1][1]:
        print("?")
    else:
        print(cc[0][0])
elif l == 2:
    print(cc[0][0])
elif l == 1:
    print("?")
