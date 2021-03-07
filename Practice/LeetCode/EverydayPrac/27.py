# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
# 动规
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         n = len(s)
#         f = [[True] * n for _ in range(n)]
#
#         for i in range(n - 1, -1, -1):
#             for j in range(i + 1, n):
#                 f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]
#
#         ret = list()
#         ans = list()
#
#         def dfs(i: int):
#             if i == n:
#                 ret.append(ans[:])
#                 return
#
#             for j in range(i, n):
#                 if f[i][j]:
#                     ans.append(s[i:j+1])
#                     dfs(j + 1)
#                     ans.pop()
#
#         dfs(0)
#         return ret


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret
