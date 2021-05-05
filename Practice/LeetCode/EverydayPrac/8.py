# 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
#
# 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
#
# 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
#
# 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = nums[x // n][x % n]

        return ans
        
# 找到 元素 与其下标的对应关系 直接进行赋值

# 复杂度分析
#
# 时间复杂度：O(rc)。这里的时间复杂度是在重塑矩阵成功的前提下的时间复杂度，否则当 mn \neq rc 时，
# C++ 语言中返回的是原数组的一份拷贝，本质上需要的时间复杂度为 O(mn)，而其余语言可以直接返回原数组的对象，需要的时间复杂度仅为 O(1)。
#
# 空间复杂度：O(1)。这里的空间复杂度不包含返回的重塑矩阵需要的空间。
