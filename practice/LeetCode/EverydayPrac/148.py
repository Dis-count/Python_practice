# 1449. Form Largest Integer With Digits That Add up to Target
# Given an array of integers cost and an integer target. Return the maximum integer you can paint under the following rules:
#
# The cost of painting a digit (i+1) is given by cost[i] (0 indexed).
# The total cost used must be equal to target.
# Integer does not have digits 0.
# Since the answer may be too large, return it as string.
#
# If there is no way to paint any integer given the condition, return "0".
#
# Example 1:
#
# Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
# Output: "7772"
# Explanation:  The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.
# Digit    cost
#   1  ->   4
#   2  ->   3
#   3  ->   2
#   4  ->   5
#   5  ->   6
#   6  ->   7
#   7  ->   2
#   8  ->   5
#   9  ->   5
#
# Example 2:
#
# Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
# Output: "85"
# Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.
#
# Example 3:
#
# Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
# Output: "0"
# Explanation: It's not possible to paint any integer with total cost equal to target.
#
# Example 4:
#
# Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
# Output: "32211"

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [[float("-inf")] * (target + 1) for _ in range(10)]
        where = [[0] * (target + 1) for _ in range(10)]
        dp[0][0] = 0

        for i, c in enumerate(cost):
            for j in range(target + 1):
                if j < c:
                    dp[i + 1][j] = dp[i][j]
                    where[i + 1][j] = j
                else:
                    if dp[i][j] > dp[i + 1][j - c] + 1:
                        dp[i + 1][j] = dp[i][j]
                        where[i + 1][j] = j
                    else:
                        dp[i + 1][j] = dp[i + 1][j - c] + 1
                        where[i + 1][j] = j - c

        if dp[9][target] < 0:
            return "0"

        ans = list()
        i, j = 9, target
        while i > 0:
            if j == where[i][j]:
                i -= 1
            else:
                ans.append(str(i))
                j = where[i][j]

        return "".join(ans)

# 上述代码有两处空间优化：
# 其一是滚动数组优化。由于 dp[i+1][] 每个元素值的计算只与 dp[i+1][] 和 dp[i][] 的元素值有关，因此可以使用滚动数组的方式，去掉 dp 的第一个维度。
# 其二是去掉 from 数组。在状态倒退时，直接根据 dp[j] 与 dp[j−cost[i]]+1 是否相等来判断，若二者相等则说明是从 dp[j−cost[i]] 转移而来，即选择了第 i 个数位。

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [float("-inf")] * (target + 1)
        dp[0] = 0

        for c in cost:
            for j in range(c, target + 1):
                dp[j] = max(dp[j], dp[j - c] + 1)

        if dp[target] < 0:
            return "0"

        ans = list()
        j = target
        for i in range(8, -1, -1):
            c = cost[i]
            while j >= c and dp[j] == dp[j - c] + 1:
                ans.append(str(i + 1))
                j -= c

        return "".join(ans)

# 复杂度分析
# 时间复杂度：O(n⋅target)。其中 n 是数组 cost 的长度。
# 空间复杂度：O(target)。
