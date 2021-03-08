# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
#
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
#
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
#
# 示例 1：
#
# 输入：[[1,1,0],[1,0,1],[0,0,0]]
# 输出：[[1,0,0],[0,1,0],[1,1,1]]
# 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
#
# 遍历矩阵的每一行。对于矩阵的第 ii 行，初始化 left=0 和 right=n−1，进行如下操作：
#
# 当 left < right 时，判断 A[i][left] 和 A[i][right] 是否相等，如果相等则对 A[i][left] 和 A[i][right] 的值进行反转，如果不相等则不进行任何操作；
#
# 将 left 的值加 1，将 right 的值减 1，重复上述操作，直到 left≥right；
#
# 如果 n 是奇数，则上述操作结束时，left 和 right 的值相等，都指向第 ii 行的中间元素，此时需要对中间元素的值进行反转。

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if A[i][left] == A[i][right]:
                    A[i][left] ^= 1
                    A[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                A[i][left] ^= 1
        return A
#
# 复杂度分析
#
# 时间复杂度：O(n^2)，其中 n 是矩阵 A 的行数和列数。需要遍历矩阵一次，进行翻转操作。
#
# 空间复杂度：O(1)。除了返回值以外，额外使用的空间为常数。