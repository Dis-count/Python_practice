# 28. Implement strStr()
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
# Example 3:
# Input: haystack = "", needle = ""
# Output: 0

#  暴力匹配 针对 每一个 原串 的位置 逐次移位。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            a, b = i, 0
            while b < m and haystack[a] == needle[b]:
                a += 1
                b += 1
            if b == m:
                return i
        return -1

# KMP 算法

class Solution:
    def strStr(self,s: str,p: str) -> int:
        i,j = 0,0
        m,n = len(s), len(p)
        nxt = nxt_pos(p)
        while i<m and j<n:
            # 注意 一定要有j=-1
            if j==-1 or s[i]==p[j]:
                i+=1
                j+=1
            else:
                j=nxt[j]
        return i-n if j==n else -1
    # next[i]表示p的前i个字符组成的子串p[0,..,i-1]的最长公共前后缀长度
    def nxt_pos(self, p):
        n=len(p)
        nxt = [-1]+[0]*n
        for i in range(2,n+1):
            j=nxt[i-1]
            while p[i-1]!=p[j] and j!=-1: #注意 是and
                j=nxt[j]
            nxt[i]=j+1
        return nxt
