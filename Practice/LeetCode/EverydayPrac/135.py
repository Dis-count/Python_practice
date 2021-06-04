# 525. Contiguous Array
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
#
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和字典: key为1的数量和0的数量的差值,value为对应坐标
        hashmap = {0:-1}
        # 当前1的数量和0的数量的差值
        counter = ans = 0
        for i,num in enumerate(nums):
            # 每多一个1，差值+1
            if num:
                counter += 1
            # 每多一个0，差值-1
            else:
                counter -= 1
            # 如果存在 1 和 0 的数量差值相等的地方，那么说明后者到前者之前 1 和 0 的数量相等！
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans

# 复杂度分析
#
# 时间复杂度：O(n)，其中 n 是数组 nums 的长度。需要遍历数组一次。
#
# 空间复杂度：O(n)，其中 n 是数组 nums 的长度。空间复杂度主要取决于哈希表，哈希表中存储的不同的 counter 的值不超过 n 个。
