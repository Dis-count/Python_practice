# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
#
# 如果不存在满足条件的子数组，则返回 0 。
#
# 示例 2：
#
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。

# 方法一：滑动窗口 + 有序集合
# 思路和解法
#
# 我们可以枚举每一个位置作为右端点，找到其对应的最靠左的左端点，满足区间中最大值与最小值的差不超过 \textit{limit}limit。
# 注意到随着右端点向右移动，左端点也将向右移动，于是我们可以使用滑动窗口解决本题。
#
# 为了方便统计当前窗口内的最大值与最小值，我们可以使用平衡树：
#
# 语言自带的红黑树，例如 C++ 中的 std::multiset，Java 中的 TreeMap；
#
# 第三方的平衡树库，例如 Python 中的 sortedcontainers（事实上，这个库的底层实现并不是平衡树，但各种操作的时间复杂度仍然很优秀）；
#
# 手写 Treap 一类的平衡树，例如下面的 Golang 代码。
#
# 来维护窗口内元素构成的有序集合。
#
# 代码
#
# 对于 Python 语言，力扣平台支持 sortedcontainers，但其没有默认被导入（import）。读者可以参考 Python Sorted Containers 了解该第三方库的使用方法。
from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1

        return ret

# 复杂度分析
#
# 时间复杂度：O(nlogn)，其中 n 是数组长度。向有序集合中添加或删除元素都是 O(log n) 的时间复杂度。每个元素最多被添加与删除一次。
#
# 空间复杂度：O(n)，其中 n 是数组长度。最坏情况下有序集合将和原数组等大。

# 方法二：滑动窗口 + 单调队列
# 思路和解法
#
# 在方法一中，我们仅需要统计当前窗口内的最大值与最小值，因此我们也可以分别使用两个单调队列解决本题。
#
# 在实际代码中，我们使用一个单调递增的队列 queMin 维护最小值，一个单调递减的队列 queMax 维护最大值。这样我们只需要计算两个队列的队首的差值，即可知道当前窗口是否满足条件。

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        queMax, queMin = deque(), deque()
        left = right = ret = 0

        while right < n:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()

            queMax.append(nums[right])
            queMin.append(nums[right])

            while queMax and queMin and queMax[0] - queMin[0] > limit:
                if nums[left] == queMin[0]:
                    queMin.popleft()
                if nums[left] == queMax[0]:
                    queMax.popleft()
                left += 1

            ret = max(ret, right - left + 1)
            right += 1

        return ret

# 复杂度分析
#
# 时间复杂度：O(n)，其中 n 是数组长度。我们最多遍历该数组两次，两个单调队列 入队出队 次数也均为 O(n)。
#
# 空间复杂度：O(n)，其中 n 是数组长度。最坏情况下单调队列将和原数组等大。
