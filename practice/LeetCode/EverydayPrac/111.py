# 1310. XOR Queries of a Subarray
# Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.
#
# Example 1:
#
# Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# Output: [2,7,14,8]
# Explanation:
# The binary representation of the elements in the array are:
# 1 = 0001
# 3 = 0011
# 4 = 0100
# 8 = 1000
# The XOR values for queries are:
# [0,1] = 1 xor 3 = 2
# [1,2] = 3 xor 4 = 7
# [0,3] = 1 xor 3 xor 4 xor 8 = 14
# [3,3] = 8
#
# Example 2:
#
# Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
# Output: [8,0,4,4]

#  树状数组

from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(arr), len(queries)
        c = [0] * 100009
        def lowbit(x):
            return x & -x

        def add(x,u):
            i = x
            while i <= n:
                c[i] ^= u
                i += lowbit(i)

        def query(x):
            ans = 0
            i = x
            while i:
                ans ^= c[i]
                i -= lowbit(i)
            return ans

        for i in range(1, n+1):
            add(i, arr[i-1])

        ans = [0] * m
        for i in range(m):
            ans[i] = query(queries[i][1] + 1) ^ query(queries[i][0])
        return ans

# 时间复杂度：令 arr 数组长度为 n，qs 数组的长度为 m。创建树状数组复杂度为 O(nlogn)；查询的复杂度为 O(mlogn)。整体复杂度为 O((n+m)logn)
# 空间复杂度：O(n)


#  前缀和
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor = list(accumulate([0] + arr, xor))
        return [prexor[i] ^ prexor[j + 1] for i, j in queries]


arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]
from itertools import accumulate
from operator import xor
list(accumulate([0] + arr, xor))


# 时间复杂度：令 arr 数组长度为 n，qs 数组的长度为 m。预处理前缀和数组复杂度为 O(n)；查询的复杂度为 O(m)。整体复杂度为 O(n+m)
# 空间复杂度：O(n)
