# 154. Find Minimum in Rotated Sorted Array II
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
#
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

# Example 1:
#
# Input: nums = [1,3,5]
# Output: 1

# Example 2:
#
# Input: nums = [2,2,2,0,1]
# Output: 0

class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        mid = left
        while nums[left] >= nums[right]:
            if left + 1 == right:
                mid = right
                break
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[mid]

# 时间复杂度：O(N)
# 空间复杂度：O(1)


a = Solution()
num = [2,3,4,5,0,1]
a.findMin(num)
num = [2,3,4,5,1,1,2,2]
a.findMin(num)
