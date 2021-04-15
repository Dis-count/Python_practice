# 给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
#
# 返回该 最大总和 。


# 复杂度分析
#
# 时间复杂度：O(nlogn)，即为对数组 nums 进行排序的时间复杂度。
#
# 空间复杂度：O(logn)，即为排序需要使用的栈空间。
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
