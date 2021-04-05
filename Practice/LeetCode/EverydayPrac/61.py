# Imagine a histogram (bar graph). Design an algorithm to compute the volume of water it could hold if someone poured water across the top. You can assume that each histogram bar has width 1.
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of water (blue section) are being trapped.

# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# 1. 暴力解法
class Solution(object):
    def trap(self, height):
        res = 0
        # 第 0 个位置和 最后一个位置不能蓄水，所以不用计算
        for i in range(1, len(height) - 1):
            # 求右边的最高柱子
            rHeight = max(height[i + 1:])
            # 求左边的最高柱子
            lHeight = max(height[:i])
            # 左右两边最高柱子的最小值 - 当前柱子的高度
            h = min(rHeight, lHeight) - height[i]
            # 如果能蓄水
            if h > 0:
                res += h
        return res

# 时间复杂度：O(N^2)
# 空间复杂度：O(1)

# 2. 动态规划

class Solution(object):
    def trap(self, height):
        N = len(height)
        # 如果小于等于两个柱子，是无法蓄水的
        if N <= 2: return 0
        # 求每个位置左边的最高柱子
        lHeight = [0] * N
        # lHeight 第 0 个位置初始化为 height[0]
        lHeight[0] = height[0]
        # 求每个位置右边的最高柱子
        rHeight = [0] * N
        # rHeight 最后一个位置初始化为 height[N - 1]
        rHeight[N - 1] = height[N - 1]
        # 求每个位置左边最高柱子高度
        for i in range(1, N):
            lHeight[i] = max(lHeight[i - 1], height[i])
        # 求每个位置右边最高柱子高度
        for i in range(N - 2, -1, -1):
            rHeight[i] = max(rHeight[i + 1], height[i])
        res = 0
        # 这个思路和上面的暴力解法一样的
        for i in range(1, len(height) - 1):
            h = min(rHeight[i], lHeight[i]) - height[i]
            if h > 0:
                res += h
        return res

# 时间复杂度：O(N)
# 空间复杂度：O(N)

# 3. 双指针
class Solution(object):
    def trap(self, height):
        N = len(height)
        if N < 2: return 0
        left, right = 0, N - 1
        lHeight = rHeight = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < lHeight:
                    res += lHeight - height[left]
                else:
                    lHeight = height[left]
                left += 1
            else:
                if height[right] < rHeight:
                    res += rHeight - height[right]
                else:
                    rHeight = height[right]
                right -= 1
        return res

# 时间复杂度：O(N)
# 空间复杂度：O(1)
