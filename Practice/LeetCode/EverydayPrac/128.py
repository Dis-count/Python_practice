# 477. Total Hamming Distance
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.
#
# Example 1:
#
# Input: nums = [4,14,2]
# Output: 6
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case).
# The answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
#
# Example 2:
#
# Input: nums = [4,14,4]
# Output: 4

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans

# 复杂度分析
# 时间复杂度：O(n⋅L)。其中 n 是数组 nums 的长度，L=30。
# 空间复杂度：O(1)。
