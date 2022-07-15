def solution(n):
    ans = ""
    lst = ["1", "2"]

    while n != 0:
        a = n % 3
        n = n // 3
        if a == 0:
            ans = "4" + ans
            n -= 1
        else:
            ans = lst[a - 1] + ans

    return ans
