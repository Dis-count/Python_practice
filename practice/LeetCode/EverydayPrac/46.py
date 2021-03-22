# 73. 矩阵置零
#
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用
# 原地 算法。
#
# 进阶：
#
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？
#
# 示例 1：
#
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]

# 原地算法：即在函数的输入矩阵上直接修改，而不是 return 一个矩阵。所以，力扣判定程序正确性的时候，仍然根据同一个 matrix 变量来判定。力扣判定的代码类似于：
#
# matrix = [输入矩阵]
# setZeroes(matrix)
# assert matrix 与预期矩阵相等

# 1.1 复制原数组
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        M, N = len(matrix), len(matrix[0])
        matrix_copy = copy.deepcopy(matrix)
        for i in range(M):
            for j in range(N):
                if matrix_copy[i][j] == 0:
                    for k in range(M):
                        matrix[k][j] = 0
                    for k in range(N):
                        matrix[i][k] = 0

# 时间复杂度：O(MN*(M+N))
# 空间复杂度：O(MN)

# 空间复杂度 O(M + N) 的算法
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        M, N = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(M):
            for j in range(N):
                if i in row or j in col:
                    matrix[i][j] = 0

# 时间复杂度：O(MN)
# 空间复杂度：O(M+N)

# 空间复杂度 O(1) 的算法
# 关键思想: 用matrix第一行和第一列记录该行该列是否有0,作为标志位
#
# 但是对于第一行,和第一列要设置一个标志位,为了防止自己这一行(一列)也有0的情况.注释写在代码里,直接看代码很好理解!

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        #print(matrix)
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0
