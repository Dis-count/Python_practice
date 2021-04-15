# 213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
#
# Example 2:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 3:
#
# Input: nums = [0]
# Output: 0

# 技巧：分别在 nums[0:N-1] 和 nums[1:N] 上计算能获取到的最大值，这两种情况取最大。这肯定能保证在物理上隔离了首尾两个元素，肯定不会同时选到。

class Solution(object):
    def rob(self, nums):
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        return max(self.rob1(nums[0:N - 1]), self.rob1(nums[1:N]))

    def rob1(self, nums):
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

# 时间复杂度：O(N)
# 空间复杂度：O(N)
