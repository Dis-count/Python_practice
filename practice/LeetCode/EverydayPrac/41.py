# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
#
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
#
# 题目数据保证答案符合 32 位带符号整数范围。

# 示例 1：
#
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^

# 其中 dp[i][j] 表示在 s[i:] 的子序列中 t[j:] 出现的个数。

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]


# 复杂度分析
#
# 时间复杂度：O(mn)，其中 m 和 n 分别是字符串 s 和 t 的长度。二维数组 dp 有 m+1 行和 n+1 列，需要对 dp 中的每个元素进行计算。
#
# 空间复杂度：O(mn)，其中 m 和 n 分别是字符串 s 和 t 的长度。创建了 m+1 行 n+1 列的二维数组 dp。
