import sys

word = sys.stdin.readline().rstrip()
l = len(word)
dic = {}
for i in range(l):
    if dic.get(word[i], -1) == -1:
        dic[word[i]] = i

for s in range(ord("a"), ord("a") + 26):
    print(dic.get(chr(s), -1))
