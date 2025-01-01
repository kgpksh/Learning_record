class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] is '0' else 0
        right = 0
        length = len(s)
        for idx in range(1, length) :
            right += s[idx] == '1'

        result = left + right
        
        for idx in range(1, length - 1) :
            left += s[idx] == '0'
            right -= s[idx] == '1'
            result = max(result, left + right)

        return result