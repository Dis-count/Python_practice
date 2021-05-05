# 740. Delete and Earn
# Given an array nums of integers, you can perform operations on the array.
#
# In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
#
# You start with 0 points. Return the maximum number of points you can earn by applying such operations.
#
#
# Example 1:
#
# Input: nums = [3,4,2]
# Output: 6
# Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points.
# 6 total points are earned.
#
# Example 2:
#
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.

#  动态规划

# 定义 f[i][0] 代表数值为 i 的数字「不选择」的最大价值；f[i][1] 代表数值为 i 的数字「选择」的最大价值。

# f[i][0]：当数值 i 不被选择，那么前一个数「可选/可不选」，在两者中取 max 即可。
# 转移方程为 f[i][0] = max(f[i−1][0],f[i−1][1])
#
# f[i][1]：当数值 i 被选，那么前一个数只能「不选」，同时为了总和最大数值 i 要选就全部选完。转移方程为
# f[i][1]=f[i−1][0]+i∗cnts[i]

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts = [0] * 10009
        n = len(nums)
        m = 0
        for x in nums:
            cnts[x] += 1
            m = max(m, x)
        # f[i][0] 代表「不选」数值 i；f[i][1] 代表「选择」数值 i
        f = [[0] * 2 for _ in range(m+1)]
        for i in range(1, m+1):
            f[i][1] = f[i-1][0] + i * cnts[i]
            f[i][0] = max(f[i-1][1], f[i-1][0])
        return max(f[m][0], f[m][1])

# 时间复杂度：遍历 nums 进行计数和取最大值 max，复杂度为 O(n)；
# 共有 max∗2 个状态需要被转移，每个状态转移的复杂度为 O(1)。整体复杂度为 O(n+max)。
# 空间复杂度：O(n)
