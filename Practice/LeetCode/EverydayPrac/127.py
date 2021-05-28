# 461. Hamming Distance
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, return the Hamming distance between them.
#
# Example 1:
#
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# Example 2:
#
# Input: x = 3, y = 1
# Output: 1

# 法一: 内置位计数功能

# 复杂度分析
# 时间复杂度：O(1)。不同语言的实现方法不一，我们可以近似认为其时间复杂度为 O(1)。
# 空间复杂度：O(1)。

# 法二: 移位实现位计数

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = x^y
        res = 0
        while s:
            res += s & 1
            s >>= 1
        return res

x = 1
y = 4
a = Solution()
a.hammingDistance(x,y)

# 复杂度分析
# 时间复杂度：O(logC)，其中 C 是元素的数据范围，在本题中 \log C=\log 2^{31} = 31 。
# 空间复杂度：O(1)。


# 法三: Brian Kernighan 算法
#  记 f(x) 表示 x 和 x−1 进行与运算所得的结果（即 f(x)=x & (x−1)），那么 f(x) 恰为 x 删去其二进制表示中最右侧的 1 的结果。

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = x^y
        res = 0
        while s:
            s = s & (s-1)
            res += 1
        return res

x = 3
y = 4
a = Solution()
a.hammingDistance(x,y)
