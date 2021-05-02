# 137. Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
#
# Example 1:
#
# Input: nums = [2,2,3,2]
# Output: 3
#
# Example 2:
#
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
#
# 方法一： 遍历统计 哈希表
from typing import List
import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans

nums = [0,1,0,1,0,1,99]
a = Solution()
a.singleNumber(nums)

# 时间复杂度：O(n)，其中 n 是数组的长度。
# 空间复杂度：O(n)。哈希映射中包含最多 ⌊n/3⌋+1 个元素，即需要的空间为 O(n)。

#  方法二： 依次确定每一个二进制位

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)  # 位运算位置
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

# 时间复杂度：O(nlogC)，其中 n 是数组的长度，C 是元素的数据范围，在本题中 \log C=\log 2^{32} = 32，
# 也就是我们需要遍历第 0∼31 个二进制位。
# 空间复杂度：O(1)。

# 方法三： 数字电路设计

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            a, b = (~a & b & num) | (a & ~b & ~num), ~a & (b ^ num)
        return b

# 方法四：  数字电路设计 优化
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b

# 时间复杂度：O(n)，其中 n 是数组的长度。
# 空间复杂度：O(1)
