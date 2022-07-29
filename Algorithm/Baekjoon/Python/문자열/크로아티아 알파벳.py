s = input()
trans = ["c=", "c-", "dz=", "d-", "nj", "lj", "s=", "z="]
for t in trans:
    s = s.replace(t, "1")
print(len(s))
