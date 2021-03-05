# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,1]

class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits

# 动态规划——最高有效位
 
# 复杂度分析
#
# 时间复杂度：O(num)。对于每个数，只需要 O(1) 的时间计算「一比特数」。
#
# 空间复杂度：O(1)。除了返回的数组以外，空间复杂度为常数。
