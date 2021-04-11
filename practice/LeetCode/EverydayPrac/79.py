# 263. Ugly Number
# Given an integer n, return true if n is an ugly number.
#
# Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.
#
# Example 1:
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
#
# Example 2:
#
# Input: n = 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
#
# Example 3:
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.
#
# Example 4:
#
# Input: n = 1
# Output: true
# Explanation: 1 is typically treated as an ugly number.


class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1

# 时间复杂度：O(log(n))
# 空间复杂度：O(1)
