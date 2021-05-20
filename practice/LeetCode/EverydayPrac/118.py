# 1442. Count Triplets That Can Form Two Arrays of Equal XOR
# Given an array of integers arr.
#
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
#
# Let's define a and b as follows:
#
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
#
# Return the number of triplets (i, j and k) Where a == b.
#
# Example 1:
#
# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
#
# Example 2:
#
# Input: arr = [1,1,1,1,1]
# Output: 10
#
# Example 3:
#
# Input: arr = [2,3]
# Output: 0
#
# Example 4:
#
# Input: arr = [1,3,5,7,9]
# Output: 3
#
# Example 5:
#
# Input: arr = [7,11,12,9,5,2,7,17,22]
# Output: 8

#  1. 前缀异或

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if s[i] == s[k + 1]:
                        ans += 1

        return ans

# 时间复杂度：O(n^3) ，其中 n 是数组 arr 的长度。
# 空间复杂度：O(n)。

#  2. 前缀异或 & 哈希表
# 根据公式和「相同数值异或结果为 0」特性，我们可以知道 sum[k] 和 sum[i−1] 数值相等，因此我们可以使用「哈希表」记录每个出现过的异或结果对应的下标集合，从而实现在确定 k 的情况下，通过 O(1) 的复杂度找到所有符合条件的 i。

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        ans = 0
        for i in range(n):
            for k in range(i + 1, n):
                if s[i] == s[k + 1]:
                    ans += k - i

        return ans

# 时间复杂度：O(n^2)
# 空间复杂度：O(n)

#  哈希表  一重循环
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        cnt, total = Counter(), Counter()
        ans = 0
        for k in range(n):
            if s[k + 1] in cnt:
                ans += cnt[s[k + 1]] * k - total[s[k + 1]]
            cnt[s[k]] += 1
            total[s[k]] += k

        return ans

# 优化
# 我们可以在计算异或前缀和的同时计算答案，从而做到仅遍历 \textit{arr}arr 一次就计算出答案。

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt, total = Counter(), Counter()
        ans = s = 0

        for k, val in enumerate(arr):
            if (t := s ^ val) in cnt:
                ans += cnt[t] * k - total[t]
            cnt[s] += 1
            total[s] += k
            s = t

        return ans

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是数组 arr 的长度。
# 空间复杂度：O(n)。我们需要使用 O(n) 的空间存储两个哈希表。
