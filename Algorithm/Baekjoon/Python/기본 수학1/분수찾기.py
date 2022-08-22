i = int(input())

init = 1
adder = 1
while i > init:
    adder += 1
    init = init + adder

if adder % 2 == 1:
    m = adder - (init - i)
    s = 1 + (init - i)
else:
    m = 1 + (init - i)
    s = adder - (init - i)

print("adder : " + str(adder))
print("init : " + str(init))
print(str(s) + "/" + str(m))
