# 264. Ugly Number II
# Given an integer n, return the nth ugly number.
#
# Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.
#
# Example 1:
#
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
#
# Example 2:
#
# Input: n = 1
# Output: 1
# Explanation: 1 is typically treated as an ugly number.

# 1 最小堆

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)

# 复杂度较大 每次都添加新的元素 空间复杂度大，导致取出和添加的复杂度也增大。
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)

# 定义数组 dp，其中 dp[i] 表示第 i 个丑数，第 n 个丑数即为 dp[n]。

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]

# 时间复杂度：O(n)。需要计算数组 dp 中的 n 个元素，每个元素的计算都可以在 O(1) 的时间内完成。
# 空间复杂度：O(n)。空间复杂度主要取决于数组 dp 的大小。
