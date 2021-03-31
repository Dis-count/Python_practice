# 190. 颠倒二进制位
# 颠倒给定的 32 位无符号整数的二进制位。

# 示例 1：
#
# 输入: 00000010100101000001111010011100
#
# 输出: 00111001011110000010100101000000
#
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
# 因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。


# 方法一：循环
# 这是最容易想到的方法了，每次把 res 左移，把 n 的二进制末尾数字，拼接到结果 res 的末尾。然后把 nn 右移。

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

# 时间复杂度：O(1)
# 空间复杂度：O(1)


# 方法二：分而治之
# 有另外一种不使用循环的做法，类似于归并排序。

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;

# 时间复杂度：O(1)
# 空间复杂度：O(1)
