# 1011. Capacity To Ship Packages Within D Days
# A conveyor belt has packages that must be shipped from one port to another within D days.
#
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.
#
# Example 1:
#
# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
#
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
#
# Example 2:
#
# Input: weights = [3,2,2,4,1,4], D = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
#
# Example 3:
#
# Input: weights = [1,2,3,1,1], D = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1

# 二分解法（精确边界）

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_w, sum_w = max(weights), sum(weights)
        l, r = max(max_w, sum_w // D), sum_w
        while l < r:
            mid = (l + r) >> 1
            if self.check(weights, mid, D):
                r = mid
            else:
                l = mid + 1
        return r

    def check(self, ws, t, d):
        n = len(ws)
        i = cnt = 1
        total = ws[0]
        while i < n:
            while i < n and total + ws[i] <= t:
                total += ws[i]
                i += 1
            total = 0
            cnt += 1
        return cnt - 1 <= d

# 时间复杂度：二分范围为 [max,sum]，check 函数的复杂度为 O(n)。
# 整体复杂度为 O(n\log({\sum_{i= 0}^{n - 1}ws[i]}))
# 空间复杂度：O(1)
