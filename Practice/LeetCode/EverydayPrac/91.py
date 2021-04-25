# 377. Combination Sum IV
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
# Example 1:
#
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
#
# Example 2:
#
# Input: nums = [9], target = 3
# Output: 0

# 递归 -> 记忆化递归(从上到下) ->  动态规划(自底向上)

# 记忆化递归
class Solution(object):
    def combinationSum4(self, nums, target):
        self.dp = [-1] * (target + 1)
        self.dp[0] = 1
        return self.dfs(nums, target)

    def dfs(self, nums, target):
        if target < 0: return 0
        if self.dp[target] != -1:
            return self.dp[target]
        res = 0
        for num in nums:
            res += self.dfs(nums, target - num)
        self.dp[target] = res
        return res

# 时间复杂度：O(N∗target)，N 是 nums 的长度。对于每个 target 求解的时候，只用遍历一次 dp 数组。
# 空间复杂度：O(target)

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        res = 0
        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]

# 时间复杂度：O(N*target)，N 是 nums 的长度。两重 for 循环，循环次数分别为 target 和 N。
# 空间复杂度：O(target)
