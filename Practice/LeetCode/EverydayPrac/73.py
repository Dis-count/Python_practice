# 剑指 Offer 56 - I. 数组中数字出现的次数
# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#
# 示例 1：
#
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
#
# 示例 2：
#
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]
#  List[int] -> List[int]
import functools

class Solution:
    def singleNumbers(self, nums) :
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1 # 左移
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]

# 时间复杂度：O(n)，我们只需要遍历数组两次。
# 空间复杂度：O(1)，只需要常数的空间存放若干变量。
a = Solution()
nums = [1,2,10,4,1,4,3,3]
a.singleNumbers(nums)
