# 1482. Minimum Number of Days to Make m Bouquets
# Given an integer array bloomDay, an integer m and an integer k.
#
# We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
#
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
#
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
#
#
# Example 1:
#
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
#
# Example 2:
#
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
#
# Example 3:
#
# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here's the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.
#
# Example 4:
#
# Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
# Output: 1000000000
# Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.
#
# Example 5:
#
# Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
# Output: 9

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(mid):
            i = cnt = 0
            while i < n and cnt < m:
                cur = 1 if bloomDay[i] <= mid else 0
                j = i
                if cur > 0:
                    while cur < k and j + 1 < n and bloomDay[j+1] <= mid:
                        j += 1
                        cur += 1
                    if cur == k:
                        cnt += 1
                    i = j + 1
                else:
                    i += 1
            return cnt >= m

        n = len(bloomDay)
        if n < m * k:
            return -1
        l, r = m * k, max(bloomDay)
        while l < r:
            mid = l + r >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r

# 时间复杂度：check 函数的复杂度为 O(n)。整体复杂度为 O(nlog1e9)
# 空间复杂度：O(1)




外婆依旧昏迷未醒，妈妈每天在病房守护，姐姐在深圳照顾两个小孩。无能为力，难过了很多天，想说点什么却又不知道该说什么。

要说对家乡没感情是假的

开始思考生活的意义，人这一生也就短短几个阶段。

生子，养老

人人都希望过上
