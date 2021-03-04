# 今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
#
# 在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
#
# 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
#
# 请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

# 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# 输出：16
# 解释：
# 书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        total = sum(c for c, g in zip(customers, grumpy) if g == 0)
        maxIncrease = increase = sum(c * g for c, g in zip(customers[:X], grumpy[:X]))
        for i in range(X, n):
            increase += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            maxIncrease = max(maxIncrease, increase)
        return total + maxIncrease


上述过程可以看成维护一个长度为 X 的滑动窗口。当滑动窗口从下标范围 [i-X,i-1] 移动到下标范围 [i−X+1,i] 时，下标 i−X 从窗口中移出，下标 i 进入到窗口内。

利用上述关系，可以在 O(1) 的时间内通过 increase i−1 得到 increase i.

由于长度为 X 的子数组的最小结束下标是 X−1，因此第一个长度为 X 的子数组对应的 increase 的值为 increase X−1
​，需要通过遍历数组 customers 和 grumpy 的前 X 个元素计算得到。从 increase X 到 increase n−1 的值则可利用上述关系快速计算得到。只需要遍历数组 customers 和 grumpy 各一次即可得到 X≤i<n 的每个 increase i 的值，时间复杂度是 O(n)。

又由于计算初始的 total 的值需要遍历数组 customers 和 grumpy 各一次，因此整个过程只需要遍历数组 customers 和 grumpy 各两次，时间复杂度是 O(n)。

在上述过程中维护增加的满意顾客的最大数量，记为 maxIncrease，则满意顾客的最大总数是 total+maxIncrease。
