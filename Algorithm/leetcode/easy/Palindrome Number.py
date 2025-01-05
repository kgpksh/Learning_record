from math import log10
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        if x == 0 :
            return True

        length = int(log10(x))
        y = x
        compare = 0
        for l in range(length, -1, -1) :
            compare += (y % 10) * (10 ** l)
            y = y // 10

        return x == compare