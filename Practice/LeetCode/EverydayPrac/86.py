# 220. Contains Duplicate III
# Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
#
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
#
# Example 3:
#
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false

# 今天这个题目和「1438. 绝对差不超过限制的最长连续子数组」非常像，本题是固定长度求差值，1438 题是固定差值求长度。


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        from sortedcontainers import SortedSet
        st = SortedSet()
        left, right = 0, 0
        res = 0
        while right < len(nums):
            if right - left > k:
                st.remove(nums[left])
                left += 1
            index = bisect.bisect_left(st, nums[right] - t)
            if st and index >= 0 and index < len(st) and abs(st[index] - nums[right]) <= t:
                return True
            st.add(nums[right])
            right += 1
        return False

# 时间复杂度：O(N*log(min(n, k)))O(N∗log(min(n,k)))，每个元素遍历一次，新元素插入红黑树的调整时间为 O(log(x))O(log(x))，set 中最多有 min(n, k)min(n,k) 个元素；
# 空间复杂度：O(min(n, k))O(min(n,k))。
