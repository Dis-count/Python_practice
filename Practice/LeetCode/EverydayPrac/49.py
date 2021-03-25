# 456. 132 模式
#
# 给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数
# nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
#
# 如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
#
# 进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？
#
# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：false
# 解释：序列中不存在 132 模式的子序列。
#
# 示例 2：
#
# 输入：nums = [3,1,4,2]
# 输出：true
# 解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
#
# 示例 3：
#
# 输入：nums = [-1,3,2,0]
# 输出：true
# 解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。

# brute force

# 时间复杂度：O(N^2)
# 空间复杂度：O(1)

class Solution(object):
    def find132pattern(self, nums):
        N = len(nums)
        numsi = nums[0]
        for j in range(1, N):
            for k in range(N - 1, j, -1):
                if numsi < nums[k] and nums[k] < nums[j]:
                    return True
            numsi = min(numsi, nums[j])
        return False

# 方法二：使用单调栈维护 3

# 求任何位置的左边最小的元素 nums[i] ，可以提前遍历一次而得到；
# 使用「单调递减栈」，把 nums[j]  入栈时，需要把栈里面比它小的元素全都 pop 出来，由于越往栈底越大，所以 pop 出的最后一个元素，就是比 3 小的最大元素 nums[k] 。
# 判断如果 nums[i] < nums[k]，那就说明得到了一个 132 模式。

class Solution(object):
    def find132pattern(self, nums):
        N = len(nums)
        leftMin = [float("inf")] * N
        for i in range(1, N):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
        stack = []
        for j in range(N - 1, -1, -1):
            numsk = float("-inf")
            while stack and stack[-1] < nums[j]:
                numsk = stack.pop()
            if leftMin[j] < numsk:
                return True
            stack.append(nums[j])
        return False

# 时间复杂度：O(N)
# 空间复杂度：O(N)
