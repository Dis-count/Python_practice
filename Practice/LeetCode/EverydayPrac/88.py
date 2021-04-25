# 91. Decode Ways
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
#
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
# Example 1:
#
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
#
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
#
# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with 0.
# The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
# Hence, there are no valid ways to decode this since all digits need to be mapped.
#
# Example 4:
#
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


# 动态规划

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        s = ' ' + s
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1,n + 1):
            a = ord(s[i]) - ord('0')
            b = ( ord(s[i - 1]) - ord('0') ) * 10 + ord(s[i]) - ord('0')
            if 1 <= a <= 9:
                f[i] = f[i - 1]
            if 10 <= b <= 26:
                f[i] += f[i - 2]
        return f[n]

#  空间优化

# 不难发现，我们转移 f[i] 时只依赖 f[i-1] 和 f[i-2] 两个状态。
# 因此我们可以采用与「滚动数组」类似的思路，只创建长度为 3 的数组，通过取余的方式来复用不再需要的下标。

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        s = ' ' + s   # One Space
        f = [0] * 3
        f[0] = 1
        for i in range(1,n + 1):
            # f[i % 3] = 0
            a = ord(s[i]) - ord('0')
            b = ( ord(s[i - 1]) - ord('0') ) * 10 + ord(s[i]) - ord('0')
            if 1 <= a <= 9:
                f[i % 3] = f[(i - 1) % 3]
            if 10 <= b <= 26:
                f[i % 3] += f[(i - 2) % 3]
        return f[n % 3]

# 时间复杂度：共有 n 个状态需要被转移。复杂度为 O(n)。
# 空间复杂度：O(1)。

aa = Solution()
s = "2226"
aa.numDecodings(s)
