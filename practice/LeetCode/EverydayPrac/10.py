# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
#
# 返回仅包含 1 的最长（连续）子数组的长度。
#
# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 前言
# 对于数组 A 的区间 [left,right] 而言，只要它包含不超过 K 个 0，我们就可以根据它构造出一段满足要求，并且长度为 right−left+1 的区间。
#
# 因此，我们可以将该问题进行如下的转化，即：
#
# 对于任意的右端点 right，希望找到最小的左端点 left，使得 [left,right] 包含不超过 K 个 0。
#
# 只要我们枚举所有可能的右端点，将得到的区间的长度取最大值，即可得到答案。
#
# 要想快速判断一个区间内 0 的个数，我们可以考虑将数组 A 中的 0 变成 1，1 变成 0。此时，我们对数组 A 求出前缀和，记为数组 P，那么 [left,right] 中包含不超过 K 个 1（注意这里就不是 0 了），当且仅当二者的前缀和之差：
#
# P[right]−P[left−1]  小于等于 K。这样一来，我们就可以容易地解决这个问题了。

# 二分查找
from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        P = [0]
        for num in A:
            P.append(P[-1] + (1 - num))

        ans = 0
        for right in range(n):
            left = bisect.bisect_left(P, P[right + 1] - K)
            ans = max(ans, right - left + 1)

        return ans

# 复杂度分析
#
# 时间复杂度：O(nlogn)，其中 n 是数组 A 的长度。每一次二分查找的时间复杂度为 O(logn)，
# 我们需要枚举 right 进行 n 次二分查找，因此总时间复杂度为 O(nlogn)。
#
# 空间复杂度：O(n)，即为前缀和数组 P 需要的空间。

# 滑动窗口
# 我们继续观察 (1) 式，由于前缀和数组 P 是单调递增的，那么 (1) 式的右侧 P[right]−K 同样也是单调递增的。因此，我们可以发现：
# 随着 right 的增大，满足 (1) 式的最小的 left 值是单调递增的。
#
# 这样一来，我们就可以使用滑动窗口来实时地维护 left 和 right 了。在 right 向右移动的过程中，我们同步移动 left，直到 left 为首个（即最小的）满足 (1) 式的位置，此时我们就可以使用此区间对答案进行更新了。
#
# 细节
#
# 当我们使用滑动窗口代替二分查找解决本题时，就不需要显式地计算并保存出前缀和数组了。我们只需要知道 left 和 right 作为下标在 前缀和数组 中对应的值，因此我们只需要用两个变量 lsum 和 rsum 记录 left 和 right 分别对应的前缀和即可。

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        left = lsum = rsum = 0
        ans = 0

        for right in range(n):
            rsum += 1 - A[right]
            while lsum < rsum - K:
                lsum += 1 - A[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans


# 复杂度分析
#
# 时间复杂度：O(n)，其中 n 是数组 A 的长度。我们至多只需要遍历该数组两次（左右指针各一次）。
#
# 空间复杂度：O(1)，我们只需要常数的空间保存若干变量。
