# 1473. Paint House III
# There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.
#
# A neighborhood is a maximal group of continuous houses that are painted with the same color.
#
# For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
# Given an array houses, an m x n matrix cost and an integer target where:
#
# houses[i]: is the color of the house i, and 0 if the house is not painted yet.
# cost[i][j]: is the cost of paint the house i with the color j + 1.
# Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.
#
# Example 1:
#
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# Output: 9
# Explanation: Paint houses of this way [1,2,2,1,1]
# This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
# Example 2:
#
# Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# Output: 11
# Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
# This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
# Cost of paint the first and last house (10 + 1) = 11.
# Example 3:
#
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
# Output: 5
# Example 4:
#
# Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
# Output: -1
# Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.

# 定义 f[i][j][k] 为考虑前 i 间房子，且第 i 间房子的颜色编号为 j，前 i 间房子形成的分区数量为 k 的所有方案中的「最小上色成本」。

# 一些编码细节：

# 下标转换：这是个人习惯，无论做什么题，我都喜欢将下标转换为从 1 开始，目的是为了「节省负值下标的分情况讨论」、「将无效状态限制在 0 下标内」或者「充当哨兵」等等。
# 将 0x3f3f3f3f 作为 INF：因为目标是求最小值，我们应当使用一个较大值充当正无穷，来关联无效状态。同时为了确保不会出现「在正无穷基础上累加导致丢失正无穷含义」的歧义情况，我们可以使用一个有「累加空间」的值作为「正无穷」（这个问题刚好最近在 这里 专门讲过）。

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = float("inf")
        f = [[[0]*(target+1) for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                f[i][j][0] = INF
        for i in range(1,m+1):
            color = houses[i-1]
            for j in range(1,n+1):
                for k in range(1,target+1):
                    if k>i:
                        f[i][j][k] = INF
                        continue
                    if color!=0: #已经上色
                        if j==color:
                            tmp = INF
                            for p in range(1,n+1):
                                if p!=j:
                                    tmp = min(tmp,f[i-1][p][k-1]) # 有新分区里的最小
                            f[i][j][k] = min(f[i-1][j][k],tmp) # 没有新分区 or 有新分区
                        else:
                            f[i][j][k] = INF
                    # 房间没上色
                    else:
                        u = cost[i-1][j-1]
                        tmp = INF
                        # 形成新分区的最优情况
                        for p in range(1,n+1):
                            if p!=j:
                                tmp = min(tmp,f[i-1][p][k-1])
                        # 算上没有新分区
                        f[i][j][k] = min(f[i-1][j][k],tmp)+u
        res = INF
        for i in range(1,n+1):
            res = min(res,f[m][i][target])
        return -1 if res == INF else res

# 时间复杂度：共有 m∗n∗t 个状态需要被转移，每次转移需要枚举「所依赖的状态」的颜色，复杂度为 O(n)。整体复杂度为 O(m * n^2 * t)
# 空间复杂度：O(m∗n∗t)


#  技巧  爆搜 需要三个参数 ->  动态规划参数

# 记忆化搜索

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(idx, color, t):
            if t < 0 or t > m - idx:
                return float("inf")
            if idx == m:
                return 0
            curr = float("inf")
            if houses[idx]:
                if houses[idx] != color:
                    curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
                else:
                    curr = min(curr, dfs(idx + 1, houses[idx], t))
            else:
                for i in range(1, n + 1):
                    if i != color:
                        curr = min(curr, dfs(idx + 1, i, t - 1) + cost[idx][i - 1])
                    else:
                        curr = min(curr, dfs(idx + 1, i, t) + cost[idx][i - 1])
            return curr

        res = dfs(0, 0, target)
        if res == float("inf"):
            return -1
        return res
