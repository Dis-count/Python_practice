# 179. Largest Number
# Given a list of non-negative integers nums, arrange them such that they form the largest number.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
# Example 1:
#
# Input: nums = [10,2]
# Output: "210"
#
# Example 2:
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
# Example 3:
#
# Input: nums = [1]
# Output: "1"
#
# Example 4:
#
# Input: nums = [10]
# Output: "10"

from typing import List
import functools

class Solution:
    # 先把 nums 中的所有数字转化为字符串，形成字符串数组 nums_str
    #比较两个字符串 x,y 的拼接结果 x+y 和 y+x 哪个更大，从而确定 x 和 y 谁排在前面；将 nums_str 降序排序
    # 把整个数组排序的结果拼接成一个字符串，并且返回

    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str,nums))
        compare = lambda x,y: 1 if x+y < y+x else -1
        nums_str.sort(key = functools.cmp_to_key(compare))
        res = ''.join(nums_str)
        if res[0] == '0':
            res = '0'
        return res


# 时间复杂度：O(N*log(N))
# 空间复杂度：O(N)
