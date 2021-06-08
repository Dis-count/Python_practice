# 474. Ones and Zeroes
# You are given an array of binary strings strs and two integers m and n.
#
# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
#
# A set x is a subset of a set y if all elements of x are also elements of y.
#
# Example 1:
#
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
#
# Example 2:
#
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.

#  看清楚  是所有 0,1 的和   因此是一个两维背包问题

#  1. 三维
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        Len = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in  range(m + 1)] for _ in range(Len + 1)]
        for k in range(1, Len + 1):
            cnt0 = strs[k-1].count('0')
            cnt1 = strs[k-1].count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[k][i][j] = dp[k-1][i][j]             #继承
                    if i - cnt0 >= 0 and j - cnt1 >= 0:     #可更新则更新
                        dp[k][i][j] = max(dp[k][i][j], dp[k-1][i-cnt0][j-cnt1] + 1)
        return dp[Len][m][n]

# 2. 二维空间   逆序循环

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = s.count('1')
            for i in range(m, cnt0 - 1, -1):    #0-1背包问题，内循环逆序
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-cnt0][j-cnt1] + 1)
        return dp[m][n]
