# 664. Strange Printer
# There is a strange printer with the following two special properties:
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.
#
# Example 1:
#
# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
#
# Example 2:
#
# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

# 令 f[i][j] 表示打印完成区间 [i,j] 的最少操作数。

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for L in range(n-1, -1, -1):      #L依赖于右侧
            for R in range(L + 1, n):   #R依赖于左侧
                if s[L] == s[R]:
                    dp[L][R] = dp[L][R-1]
                else:
                    tmp = 1000
                    for mid in range(L, R, 1):
                        tmp = min(tmp, dp[L][mid] + dp[mid+1][R])
                    dp[L][R] = tmp
        return dp[0][n-1]

# 复杂度分析
# 时间复杂度：O(n^3)，其中 n 是字符串的长度。
# 空间复杂度：O(n^2)，其中 n 是字符串的长度。我们需要保存所有 n^2 个状态。
