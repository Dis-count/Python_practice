# 给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
#
# 实现 NumArray 类：

# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）

# 如果根据题意直接进行求解的话，复杂度比较大因而 需要用动态规划 转化一下  这样每次检索 复杂度都是1

# 方法: 前缀和

# 输入：
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# 输出：
# [null, 1, -1, -3]

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]

# 复杂度分析
#
# 时间复杂度：初始化 O(n)，每次检索 O(1)，其中 n 是数组 nums 的长度。
# 初始化需要遍历数组 nums 计算前缀和，时间复杂度是 O(n)。
# 每次检索只需要得到两个下标处的前缀和，然后计算差值，时间复杂度是 O(1) 。
#
# 空间复杂度：O(n)，其中 n 是数组 nums 的长度。需要创建一个长度为 n+1 的前缀和数组。
