# 633. Sum of Square Numbers
# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
#
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
#
# Example 2:
#
# Input: c = 3
# Output: false
#
# Example 3:
#
# Input: c = 4
# Output: true
#
# Example 4:
#
# Input: c = 2
# Output: true
#
# Example 5:
#
# Input: c = 1
# Output: true

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0: return True
        for a in range(1, int(math.sqrt(c) + 1)):
            b = c - a * a
            if int(math.sqrt(b)) ** 2 == b:
                return True
        return False

# 时间复杂度：O(sqrt(c))
# 空间复杂度：O(1)


#  双指针

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            cur = l * l + r * r
            if cur == c:
                return True
            elif cur > c:
                r -= 1
            else:
                l += 1
        return False

#  费马平方和定理的转化还不太清楚
