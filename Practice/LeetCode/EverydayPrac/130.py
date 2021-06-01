# 231. Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2^x.
#
# Example 1:
#
# Input: n = 1
# Output: true
# Explanation: 20 = 1
#
# Example 2:
#
# Input: n = 16
# Output: true
# Explanation: 24 = 16
#
# Example 3:
#
# Input: n = 3
# Output: false
#
# Example 4:
#
# Input: n = 4
# Output: true
#
# Example 5:
#
# Input: n = 5
# Output: false

# 法一： 朴素解法


# 法二： lowbit  (n & -n)
# 熟悉树状数组的同学都知道，lowbit 可以快速求得 x 二进制表示中最低位 1 表示的值。
# 如果一个数 n 是 2 的幂，那么有 lowbit(n) = n 的性质（2 的幂的二进制表示中必然是最高位为 1，低位为 0）。

# 法三： 二进制 位运算 (n & n-1 = 0)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n = 0:
            return False
        else:
            return (n & (n-1) == 0)

a = Solution()
n = 16
a.isPowerOfTwo(n)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n

# 复杂度分析
# 时间复杂度：O(1)。
# 空间复杂度：O(1)。
