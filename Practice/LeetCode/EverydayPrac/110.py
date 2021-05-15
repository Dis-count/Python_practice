# 1734. Decode XORed Permutation
# There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.
#
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].
#
# Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.
#
# Example 1:
#
# Input: encoded = [3,1]
# Output: [1,2,3]
# Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
#
# Example 2:
#
# Input: encoded = [6,5,4,6]
# Output: [2,4,1,5,3]

# 注意 之前的题目  得到第一位就可以得到 结果。
# 同时 注意 n 是 odd。因此 隔位异或可以得到 好的结果。

from typing import List
from functools import reduce
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = reduce(xor, range(1, n + 1))
        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]

        perm = [total ^ odd]
        for i in range(n - 1):
            perm.append(perm[-1] ^ encoded[i])

        return perm

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是原始数组 perm 的长度。计算 total 和 odd 各需要遍历长度为 n−1 的数组 encoded 一次，计算原数组 perm 的每个元素值也需要遍历长度为 n-1 的数组 encoded 一次。
# 空间复杂度：O(1)。注意空间复杂度不考虑返回值。

import operator
n = 10
total = reduce(operator.xor, range(1, n + 1))
