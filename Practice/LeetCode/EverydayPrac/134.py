# 1744. Can You Eat Your Favorite Candy on Your Favorite Day?
# You are given a (0-indexed) array of positive integers candiesCount where candiesCount[i] represents the number of candies of the ith type you have. You are also given a 2D array queries where queries[i] = [favoriteTypei, favoriteDayi, dailyCapi].
#
# You play a game with the following rules:
#
# You start eating candies on day 0.
# You cannot eat any candy of type i unless you have eaten all candies of type i - 1.
# You must eat at least one candy per day until you have eaten all the candies.
# Construct a boolean array answer such that answer.length == queries.length and answer[i] is true if you can eat a candy of type favoriteTypei on day favoriteDayi without eating more than dailyCapi candies on any day, and false otherwise. Note that you can eat different types of candy on the same day, provided that you follow rule 2.
#
# Return the constructed array answer.
#
# Example 1:
#
# Input: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
# Output: [true,false,true]
# Explanation:
# 1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you will eat a candy of type 0 on day 2.
# 2- You can eat at most 4 candies each day.
#    If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and 4 candies (type 0 and type 1) on day 1.
#    On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a candy of type 4 on day 2.
# 3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.
#
# Example 2:
#
# Input: candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
# Output: [false,true,true,false,false]

# 读者需要注意的题目中的一个小陷阱：我们是从第 0 天开始吃糖果。因此对于第 i 个询问，我们可以吃 favoriteDay_i+1 天的糖果。

#  前缀和  其实就是要找  查询区间 和 可行区间的 重叠区域  重叠即可 true

# 可吃糖果数量区间 [favoriteDayi+1,(favoriteDayi+1)×dailyCapi]
#  只要包含 所需类型的糖果即可

#  因此需要求出 糖果数量前缀和 第 i 种类型的糖果对应编号为
# [sum[favoriteTypei​ −1]+1, sum[favoriteTypei]]

# 判断是否有交集

from typing import List
from itertools import *

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # 前缀和
        total = list(accumulate(candiesCount))

        ans = list()
        for favoriteType, favoriteDay, dailyCap in queries:
            x1 = favoriteDay + 1
            y1 = (favoriteDay + 1) * dailyCap
            x2 = 1 if favoriteType == 0 else total[favoriteType - 1] + 1
            y2 = total[favoriteType]

            ans.append(not(x1 > y2 or y1 < x2))

        return ans

candiesCount = [5,2,6,4,1]


# 复杂度分析
# 时间复杂度：O(n+q)，其中 n 和 q 分别是数组 candiesCount 和 queries 的长度。我们需要 O(n) 的时间计算前缀和，O(q) 的时间得到所有询问的结果。
# 空间复杂度：O(n)，即为存储前缀和数组需要的空间。注意返回值不计入空间复杂度。
