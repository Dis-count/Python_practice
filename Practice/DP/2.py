# 类型二：求数组的最大值
#
# Longest Increasing Subsequence
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) < 2:
            return len(nums)
        temp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and temp[i] < temp[j]+1:
                    temp[i] = temp[j]+1
        return max(temp)

s = Solution()
sum = [10,9,2,5,3,7,9,101,18]
s.lengthOfLIS(sum)
