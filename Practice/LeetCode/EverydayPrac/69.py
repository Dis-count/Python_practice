# 81. Search in Rotated Sorted Array II
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
#
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
#
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
#
# Example 1:
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
# Example 2:
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

class Solution(object):
    def search(self, nums, target):
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[right]:
                left += 1
                continue
            if nums[mid] <= nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

# 时间复杂度：O(log(N))
# 空间复杂度：O(1)
