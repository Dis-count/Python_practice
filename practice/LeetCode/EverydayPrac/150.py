# 523. Continuous Subarray Sum
# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.
#
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
#
# Example 1:
#
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
#
# Example 2:
#
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
#
# Example 3:
#
# Input: nums = [23,2,6,4,7], k = 13
# Output: false

#  前缀和 + 哈希表
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            # 当前前缀和
            presum += num
            presum %= k
            # 同余定理
            if presum in modes:
                return True
            # 上一个前缀和，下一个就可以用了（距离为2了）
            modes.add(last)
        return False

# 在 python 中 用字典 或者 set 来存储之前的和
nums = [23,2,6,4,7]
k = 6
