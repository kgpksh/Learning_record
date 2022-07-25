def solution(s):
    list = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for i, letter in enumerate(list):
        s = s.replace(letter, str(i))
    return int(s)
