# 剑指 Offer 56 - II. 数组中数字出现的次数 II
# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
#
# 示例 1：
#
# 输入：nums = [3,4,3,3]
# 输出：4
#
# 示例 2：
#
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
# : List[int] -> int
class Solution:
    def singleNumber(self, nums) :
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

a =Solution()
nums = [3,4,4,4]
a.singleNumber(nums)

# 时间复杂度 O(N) ： 其中 N 位数组 nums 的长度；遍历数组占用 O(N) ，每轮中的常数个位运算操作占用 O(32×3×2)=O(1) 。
# 空间复杂度 O(1) ： 变量 ones , twos 使用常数大小的额外空间。
