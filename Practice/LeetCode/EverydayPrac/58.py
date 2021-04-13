# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]

#  回溯法  39/40/46/47/78/90

# 其实回溯算法关键在于:不合适就退回上一步

# 然后通过约束条件, 减少时间复杂度.
# 嵌套定义
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res

# 方法二： 迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
# ---------------------------------------

class Solution(object):
    def subsets(self, nums):
        res, path = [], []
        self.dfs(nums, 0, res, path)
        return res

    def dfs(self, nums, index, res, path):
        res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()


class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])
