# 1074. Number of Submatrices That Sum to Target
# Given a matrix and a target, return the number of non-empty submatrices that sum to target.
#
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
#
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
#
# Example 1:
#
# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
#
# Example 2:
#
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

# Example 3:
#
# Input: matrix = [[904]], target = 0
# Output: 0

# 方法一：前缀和 + 哈希表
# 我们枚举子矩阵的上下边界，并计算出该边界内每列的元素和，则原问题转换成了如下一维问题：
# 给定一个整数数组和一个整数 target，计算该数组中子数组和等于 target 的子数组个数。

from typing import List
from collections import Counter

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])
            count = pre = 0
            for x in nums:
                pre += x
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count

        m, n = len(matrix), len(matrix[0])
        ans = 0
        # 枚举上边界
        for i in range(m):
            total = [0] * n
            # 枚举下边界
            for j in range(i, m):
                for c in range(n):
                    # 更新每列的元素和
                    total[c] += matrix[j][c]
                ans += subarraySum(total, target)

        return ans

# 复杂度分析
# 时间复杂度：O(m^2⋅n)。其中 m 和 n 分别是矩阵 matrix 的行数和列数。
# 空间复杂度：O(n)。

#  下面这个方法非常精妙  用于找到 所有连续子数组的和
def subarraySum(nums: List[int], k: int) -> int:
    mp = Counter([0])
    count = pre = 0
    for x in nums:
        pre += x
        if pre - k in mp:
            count += mp[pre - k]
        mp[pre] += 1
    return count
