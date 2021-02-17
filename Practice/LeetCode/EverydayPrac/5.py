# 方法二：广度优先搜索
# 我们也可以通过广度优先搜索的方式，求解图中的连通分量。
#
# 起初，我们将每个节点都标记为「未访问」，并遍历图中的每个节点。如果发现一个「未访问」的节点，就从该节点出发，沿着图中的边，将其余的「未访问」的节点都标记为「已访问」，并同时统计标记的次数。当遍历过程终止时，标记的数量次数即为连通分量的大小。
#
# 复杂度分析
#
# 时间复杂度：O(N)，其中 N 为情侣的总数。每个节点最多只被标记 1 次。
#
# 空间复杂度：O(N)，其中 N 为情侣的总数。为队列的开销。


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        pos = {val:i for i,val in enumerate(row)}
        ans = 0
        for i in range(1,N,2):
            while row[i-1] != row[i] ^ 1:
                enchange_index = pos[row[i] ^ 1] ^ 1
                row[i], row[enchange_index] = row[enchange_index], row[i]
                ans += 1
        return ans
