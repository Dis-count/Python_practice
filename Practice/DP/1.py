# 类型一：迭代至最后一个值输出
#
# 零钱兑换
#
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        dp = [0 for i in range(amount+1)]
        for subAmount in range(1, amount+1):
            temp = []
            for coin in coins:
                if subAmount >= coin and dp[subAmount - coin] != -1:
                    temp.append(dp[subAmount - coin]+1)
            dp[subAmount] = min(temp) if len(temp) > 0 else -1
        if dp[-1] > 0:
            return dp[-1]
        elif amount == 0:
            return 0
        else:
            return -1

s=Solution()
coins = [1, 2, 5]
amount = 11
s.coinChange(coins,amount)
