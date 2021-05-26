# 1787. Make the XOR of All Segments Equal to Zero
# You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].
#
# Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.
#
# Example 1:
#
# Input: nums = [1,2,0,3,0], k = 1
# Output: 3
# Explanation: Modify the array from [1,2,0,3,0] to [0,0,0,0,0].
#
# Example 2:
#
# Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
# Output: 3
# Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
#
# Example 3:
#
# Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
# Output: 3
# Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # x 的范围为 [0, 2^10)
        MAXX = 2**10

        n = len(nums)
        f = [float("inf")] * MAXX
        # 边界条件 f(-1,0)=0
        f[0] = 0

        for i in range(k):
            # 第 i 个组的哈希映射
            count = Counter()
            size = 0
            for j in range(i, n, k):
                count[nums[j]] += 1
                size += 1

            # 求出 t2
            t2min = min(f)

            g = [t2min] * MAXX
            for mask in range(MAXX):
                # t1 则需要枚举 x 才能求出
                for x, countx in count.items():
                    g[mask] = min(g[mask], f[mask ^ x] - countx)

            # 别忘了加上 size
            f = [val + size for val in g]

        return f[0]
