# 1269. Number of Ways to Stay in the Same Place After Some Steps
# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).
#
# Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
#
# Example 2:
#
# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
#
# Example 3:
#
# Input: steps = 4, arrLen = 2
# Output: 8

# dp[i][j] 表示在 i 步操作之后，指针位于下标 j 的方案数

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        maxColumn = min(arrLen - 1, steps)

        dp = [[0] * (maxColumn + 1) for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(0, maxColumn + 1):
                dp[i][j] = dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                if j + 1 <= maxColumn:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod

        return dp[steps][0]

# 优化空间

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        maxColumn = min(arrLen - 1, steps)

        dp = [0] * (maxColumn + 1)
        dp[0] = 1

        for i in range(1, steps + 1):
            dpNext = [0] * (maxColumn + 1)
            for j in range(0, maxColumn + 1):
                dpNext[j] = dp[j]
                if j - 1 >= 0:
                    dpNext[j] = (dpNext[j] + dp[j - 1]) % mod
                if j + 1 <= maxColumn:
                    dpNext[j] = (dpNext[j] + dp[j + 1]) % mod
            dp = dpNext

        return dp[0]
