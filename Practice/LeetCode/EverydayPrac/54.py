# 74. 搜索二维矩阵
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false

# 方法一：遍历
class Solution(object):
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)

# 方法二：从左下角或者右上角开始查找

# 从右上角开始遍历：
# 如果要搜索的 target 比当前元素大，那么让行增加；
# 如果要搜索的 target 比当前元素小，那么让列减小；

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False

# 时间复杂度：O(M + N)
# 空间复杂度：O(1)

# 方法三：先寻找到所在行

class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            if target > matrix[i][N - 1]:
                continue
            if target in matrix[i]:
                return True
        return False

# 二分查找

class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            if target > matrix[i][N - 1]:
                continue
            index = bisect.bisect_left(matrix[i], target)
            if matrix[i][index] == target:
                return True
        return False

# 时间复杂度： 在行中遍历查找的时间复杂度是： O(M+N)；在行中进行二分查找的时间复杂度是 O(M+log(N))
# 空间复杂度：O(1)

# 方法四 两次二分查找

class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        col0 = [row[0] for row in matrix]
        target_row = bisect.bisect_right(col0, target) - 1
        if target_row < 0:
            return False
        target_col = bisect.bisect_left(matrix[target_row], target)
        if target_col >= N:
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False

# 时间复杂度：O(log(M)+log(N))
# 空间复杂度：O(1)
