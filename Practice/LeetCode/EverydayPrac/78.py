# 896. Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.
#
# Example 1:
#
# Input: [1,2,2,3]
# Output: true
#
# Example 2:
#
# Input: [6,5,4,4]
# Output: true
#
# Example 3:
#
# Input: [1,3,2]
# Output: false
#
# Example 4:
#
# Input: [1,2,4,5]
# Output: true
#
# Example 5:
#
# Input: [1,1,1]
# Output: true

# M1: 两次遍历
#
# 遍历两次，分别判断是否为单调递增的数列、单调递减的数列。

class Solution:
    def isMonotonic(self, A):
        return self.isIncreasing(A) or self.isDecreasing(A)

    def isIncreasing(self, A):
        N = len(A)
        for i in range(N - 1):
            if A[i + 1] - A[i] < 0:
                return False
        return True

    def isDecreasing(self, A):
        N = len(A)
        for i in range(N - 1):
            if A[i + 1] - A[i] > 0:
                return False
        return True

# 时间复杂度：O(2∗N)=O(N)
# 空间复杂度：O(1)

# M2：一次遍历

# 也可以遍历一次：
# 使用 inc 标记数组是否单调上升的，如果有下降，则将其置为 false；
# 使用 dec 标记数组是否单调递减的，如果有上升，则将其置为 false。


class Solution:
    def isMonotonic(self, A):
        N = len(A)
        inc, dec = True, True
        for i in range(1, N):
            if A[i] < A[i - 1]:
                inc = False
            if A[i] > A[i - 1]:
                dec = False
            if not inc and not dec:
                return False
        return True

# 时间复杂度：O(N)
# 空间复杂度：O(1)
