from collections import Counter


def solution(nums):
    lst = Counter(nums)
    return min(len(lst), len(nums) / 2)
