# 1720. Decode XORed Array
# There is a hidden integer array arr that consists of n non-negative integers.
#
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
#
# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
#
# Return the original array arr. It can be proved that the answer exists and is unique.
#
#
#
# Example 1:
#
# Input: encoded = [1,2,3], first = 1
# Output: [1,0,2,1]
# Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
# Example 2:
#
# Input: encoded = [6,2,7,3], first = 4
# Output: [4,2,0,7,4]

#  其实 就是求得 XOR 的逆运算  利用数学式子 推导即可。

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        arr = [first]
        for num in encoded:
            arr.append(arr[-1] ^ num)
        return arr


# 复杂度分析
# 时间复杂度：O(n)，其中 n 是原数组 arr 的长度。需要遍历长度为 n−1 的编码数组 encoded 一次，计算原数组 arr 的每个元素值。
# 空间复杂度：O(1)。注意空间复杂度不考虑返回值。
