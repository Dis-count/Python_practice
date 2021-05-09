# 1486. XOR Operation in an Array
# Given an integer n and an integer start.
#
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
#
# Return the bitwise XOR of all elements of nums.
#
# Example 1:
#
# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.
#
# Example 2:
#
# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
#
# Example 3:
#
# Input: n = 1, start = 7
# Output: 7
#
# Example 4:
#
# Input: n = 10, start = 5
# Output: 2


#  直接模拟

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= (start + i * 2)
        return ans

a = Solution()
n = 4
start = 3
a.xorOperation(n,start)

# 复杂度分析
# 时间复杂度：O(n)。这里用一重循环对 n 个数字进行异或。
# 空间复杂度：O(1)。这里只是用了常量级别的辅助空间。

# 利用数学上的性质

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def cal(x):
            """
                4a ^ (4a + 1) = 1
                4a ^ (4a + 1) ^ (4a + 2) = 1 ^ (4a + 2) = 4a + 3
                4a ^ (4a + 1) ^ (4a + 2) ^ (4a + 3) = (4a + 3) ^ (4a + 3) = 0
            """
            if x % 4 == 0:
                return x
            elif x % 4 == 1:
                return 1
            elif x % 4 == 2:
                return x + 1
            return 0

        # 整体除以2, 利用 %4 结论计算 ans 中除「最低一位」的结果
        s = start >> 1
        # 计算 1 到 s - 1的异或结果，再计算 1 到 s + n - 1的异或结果，两者异或得到ans中除最后一位的结果
        prefix = cal(s - 1) ^ cal(s + n - 1)
        # 利用「奇偶性」计算 ans 中的「最低一位」结果
        last = n & start & 1
        return prefix << 1 | last
