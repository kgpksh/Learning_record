def solution(n, arr1, arr2):
    answer = [""] * n
    for i in range(n):
        a1 = str(format(arr1[i], "b"))
        a2 = str(format(arr2[i], "b"))

        while len(a1) < n:
            a1 = "0" + a1
        while len(a2) < n:
            a2 = "0" + a2

        for j in range(n):
            if a1[j] == "0" and a2[j] == "0":
                answer[i] += " "
            else:
                answer[i] += "#"
    return answer
