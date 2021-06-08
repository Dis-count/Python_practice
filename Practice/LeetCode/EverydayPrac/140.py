# 1049. Last Stone Weight II
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the smallest possible weight of the left stone. If there are no stones left, return 0.
#
# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
#
# Example 2:
# Input: stones = [31,26,33,21,40]
# Output: 5
#
# Example 3:
# Input: stones = [1,2]
# Output: 1

#  转化为 背包问题

# 要使最后一块石头的重量尽可能地小，neg 需要在不超过 ⌊sum/2⌋ 的前提下尽可能地大。因此本问题可以看作是背包容量为 ⌊sum/2⌋，物品重量和价值均为 stones_i 的 0-1 背包问题。

#  注意区别  上一个是求 方案数  因而需要相加  本次是 是求可能的最小值 还有可能求每次的确定最大
#  所求目标不同 得到的  状态转移方程也不同

from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n):
            for j in range(m + 1):
                if j < stones[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j] or dp[i][j - stones[i]]

        ans = None
        for j in range(m, -1, -1):
            if dp[n][j]:
                ans = total - 2 * j
                break

        return ans
#  9 // 2 == 4

# 改进

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [False] * (m + 1)
        dp[0] = True

        for weight in stones:
            for j in range(m, weight - 1, -1):
                dp[j] |= dp[j - weight]

        ans = None
        for j in range(m, -1, -1):
            if dp[j]:
                ans = total - 2 * j
                break

        return ans

# 复杂度分析
# 时间复杂度：O(n⋅sum)。其中 n 是数组 stones 的长度，sum 为 stones 所有元素之和。
# 空间复杂度：O(sum)。
