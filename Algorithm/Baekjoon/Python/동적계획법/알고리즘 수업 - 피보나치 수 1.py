n = int(input())
global recur
global dp

recur = 0
dp = 0


def fib(n):
    global recur

    if n == 1 or n == 2:
        recur += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global dp

    f = []
    f.append(1)
    f.append(1)
    for i in range(2, n):
        dp += 1
        f.append(f[i - 1] + f[i - 2])


fib(n)
fibonacci(n)
print(recur, end=" ")
print(dp)
