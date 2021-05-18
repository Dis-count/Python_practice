# 421. Maximum XOR of Two Numbers in an Array
# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.
#
# Follow up: Could you do this in O(n) runtime?
#
# Example 1:
#
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.

# Example 2:
#
# Input: nums = [0]
# Output: 0

# Example 3:
#
# Input: nums = [2,4]
# Output: 6

# Example 4:
#
# Input: nums = [8,10,2]
# Output: 10

# Example 5:
#
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            # 将所有的 pre^k(a_j) 放入哈希表中
            for num in nums:
                # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
                # 只需将其右移 k 位
                seen.add(num >> k)

            # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
            # 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
            x_next = x * 2 + 1
            found = False

            # 枚举 i
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found:
                x = x_next
            else:
                # 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
                # 即为 x = x*2
                x = x_next - 1

        return x

#  前缀树
# 分析：
# 其实每个数字还是都要和其他数字做个异或，不过利用了前缀树和贪心思想，每一步都挑一个最大的值，把其他路径都剪枝掉了。

class Trie:
    def __init__(self, val):
        self.val = val
        self.child = {}

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        #取得最大长度
        L = len(format(max(nums), 'b'))-1

        # 构建前缀树
        root = Trie(-1)

        for n in nums:
            curr = root
            for i in range(L, -1, -1):

                v = (n >> i) & 1
                if v not in curr.child:
                    curr.child[v] = Trie(v)

                curr = curr.child[v]

        res = 0

        #搜索
        for n in nums:
            curr = root
            total = 0
            for i in range(L, -1, -1):
                v = (n >> i) & 1
                if 1-v in curr.child:
                    total = total * 2 + 1
                    curr = curr.child[1-v]
                else:
                    total = total * 2
                    curr = curr.child[v]

            #print(n, total)
            res = max(res, total)

        return res

#  复杂度分析
# 构建前缀树 O(n)
# 搜索前缀树 O(n)
