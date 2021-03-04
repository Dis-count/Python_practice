# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
#
# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
#
#
# 方法一：模拟
# 创建一个 n 行 m 列的新矩阵，根据转置的规则对新矩阵中的每个元素赋值，则新矩阵为转置后的矩阵。

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed

# 复杂度分析
#
# 时间复杂度：O(mn)，其中 m 和 n 分别是矩阵 matrix 的行数和列数。需要遍历整个矩阵，并对转置后的矩阵进行赋值操作。
#
# 空间复杂度：O(1)。除了返回值以外，额外使用的空间为常数。
