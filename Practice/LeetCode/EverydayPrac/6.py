# 最大连续一的个数
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 注意：
#
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0

        maxCount = max(maxCount, count)
        return maxCount

# 复杂度分析
#
# 时间复杂度：O(n)O(n)，其中 nn 是数组的长度。需要遍历数组一次。
#
# 空间复杂度：O(1)O(1)。
