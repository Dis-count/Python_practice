# 90. Subsets II
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]

# path 全局变量
#  为了不重复添加相同元素， 需要添加一个判断
# 如果相等就不添加到 path 中。
class Solution(object):
    def subsetsWithDup(self, nums):
        res, path = [], []
        nums.sort()
        self.dfs(nums, 0, res, path)
        return res

    def dfs(self, nums, index, res, path):
        res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()

# path 每次新建
class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])
