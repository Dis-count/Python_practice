# 1802. 有界数组中指定下标处的最大值
# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
#
# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 返回你所构造的数组中的 nums[index] 。
#
# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
#
#
# 示例 1：
#
# 输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
#
# 示例 2：
#
# 输入：n = 6, index = 1,  maxSum = 10
# 输出：3

# 1.用了二分查找框架--符合条件的最右

L = min
R = max
while L < R:
    mid = (L + R + 1) >> 1
    if check(mid)是ok的，符合想要的条件的：
        L = mid
    else:
        R = mid - 1
return R

# 2.等差数列求和
#
# sum = (首项+末项)*项数//2
#
# 边界问题实在是头疼。平时静下心来，差不多也要10分钟，周赛时候无由慌张，没写对
#
# 慢慢提高能力，磨练心态吧。

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        L = 1
        R = maxSum + 1
        while L < R:            #######寻找符合条件的最右框架
            mid = (L + R + 1) >> 1
            if self.calc(mid, n, index) <= maxSum:
                L = mid
            else:
                R = mid - 1
        return R

    def calc(self, peak: int, n: int, index: int) -> int:
        L_sum = 0
        if peak > index:    # peak-index, peak-index+1,……,peak
            L_sum = (peak-index + peak) * (index + 1) // 2
        else:       #1,1,1,1,  1,2,3,peak
            L_sum = (index+1-peak)*1 + (1 + peak)*(peak)//2

        R_sum = 0
        if peak > (n-1-index):  #peak,peak-1,……,peak-(n-1-index)
            R_sum = (peak + peak-(n-1-index)) * (n-index) // 2
        else:       #peak,peak-1,……,3,2,1   1,1,1,1
            R_sum = (peak+1)*peak//2 + (n-index-peak) * 1

        return L_sum + R_sum - peak     #为了方便计算，peak算了2次
