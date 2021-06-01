# 342. Power of Four
# Given an integer n, return true if it is a power of four. Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4x.
#
# Example 1:
#
# Input: n = 16
# Output: true
#
# Example 2:
#
# Input: n = 5
# Output: false
#
# Example 3:
#
# Input: n = 1
# Output: true

#  法一： 二进制中 1 的位置位于偶数

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0

#  法二  模 3 余 1

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1

# 复杂度分析
# 时间复杂度：O(1)。
# 空间复杂度：O(1)。
