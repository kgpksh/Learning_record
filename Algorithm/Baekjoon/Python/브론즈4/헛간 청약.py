n, w, h, l = map(int,input().split())

capability = (w//l) * (h//l)

print(min(capability, n))