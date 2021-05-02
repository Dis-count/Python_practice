# 53，1262，1363

# 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, assume that your function returns 2^31 − 1 when the division result overflows.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
#
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
#
# Example 3:
#
# Input: dividend = 0, divisor = 1
# Output: 0
#
# Example 4:
#
# Input: dividend = 1, divisor = 1
# Output: 1

# 方法1：递归
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647  # [−2**31, 2**31−1]
        flag = 1                                    # 存储正负号，并将分子分母转化为正数
        if dividend < 0: flag, dividend = -flag, -dividend
        if divisor < 0: flag, divisor  = -flag, -divisor

        def div(dividend, divisor):                 # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
            if dividend < divisor:
                return 0
            cur = divisor
            multiple = 1
            while cur + cur < dividend:             # 用加法求出保证divisor * multiple <= dividend的最大multiple
                cur += cur                          # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
                multiple += multiple
            return multiple + div(dividend - cur, divisor)
        res = div(dividend, divisor)

        res = res if flag > 0 else -res             # 恢复正负号

        if res < MIN_INT:                           # 根据是否溢出返回结果
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT


# 方法2：迭代
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647  # [−2**31, 2**31−1]
        flag = 1                                    # 存储正负号，并将分子分母转化为正数
        if dividend < 0: flag, dividend = -flag, -dividend
        if divisor < 0: flag, divisor  = -flag, -divisor

        res = 0
        while dividend >= divisor:                  # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
            cur = divisor
            multiple = 1
            while cur + cur < dividend:             # 用加法求出保证divisor * multiple <= dividend的最大multiple
                cur += cur                          # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
                multiple += multiple
            dividend -= cur
            res += multiple

        res = res if flag > 0 else -res             # 恢复正负号

        if res < MIN_INT:                           # 根据是否溢出返回结果
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
