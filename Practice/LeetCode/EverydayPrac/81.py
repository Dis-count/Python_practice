# 213. House Robber I
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are not arranged in a circle. That means the first house is not the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

#  注意 状态转移一定要从 i 的定义开始， 而不是靠感觉分析，要按照范式来分析
#  比如 定义状态 i 就分析 i 处是否选择而不是分析 i-1 处是否选择 强行凑出状态转移方程。

# dp[0] = nums[0]
# dp[1] = max(dp[0], nums[1]) = max(nums[0], nums[1])
# 返回 dp[N-1]  注意下标即可。

class Solution(object):
    def rob(self, nums):
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        # max amount [0, i]
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

# 时间复杂度：O(N)
# 空间复杂度：O(N)
