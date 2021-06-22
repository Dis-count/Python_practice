# 剑指 Offer 38. 字符串的排列
# 输入一个字符串，打印出该字符串中字符的所有排列。
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  analysis:It is obvious that if all the letters are different, then we have N! results.
#  If there are the same letters, then we have to delete the repetitive results.
#  剪枝的方法 存在某一位相同的字母 则直接跳过
#  整体的方式是 深度优先算法DFS

# 递归
str ='abd'
c = list(str)

from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换
        dfs(0)
        return res
