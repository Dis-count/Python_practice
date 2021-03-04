# 给你一个整数数组 target 和一个数组 initial ，initial 数组与 target  数组有同样的维度，且一开始全部为 0 。
#
# 请你返回从 initial 得到  target 的最少操作次数，每次操作需遵循以下规则：
#
# 在 initial 中选择 任意 子数组，并将子数组中每个元素增加 1 。
# 答案保证在 32 位有符号整数以内。
#
# 示例 2：
#
# 输入：target = [3,1,1,2]
# 输出：4
# 解释：(initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target) 。

# 相信看过本题各种参考代码的读者都会抱着复杂的心情：本题是第 31 场双周赛的最后一题，难度为 困难，但只需要五行代码，即：
#
# 求出数组 target 中相邻两元素的差值，保留大于 0 的部分，累加即为答案。

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1, n):
            ans += max(target[i] - target[i - 1], 0)
        return ans

# 复杂度分析
#
# 时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{target}target 的长度。
#
# 空间复杂度：O(1)O(1)。
