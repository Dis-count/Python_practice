# 403. Frog Jump
# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
#
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
#
# Example 1:
#
# Input: stones = [0,1,3,5,6,8,12,17]
# Output: true
# Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
#
# Example 2:
#
# Input: stones = [0,1,2,3,4,8,9,11]
# Output: false
# Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.


# 状态定义和参数：s(i, step) 表示当前是第 i 块时候，通过 step 步过来的

#  记忆化递归 (带标记的深度优先 DFS)  ->  动态规划

class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if stones[1] - stones[0] > 1: return False

        stonesSet = set(stones) # 变成 Set， 加速检索

        @functools.lru_cache(None) # 加上备忘录，去掉重复计算
        def helper(i, step):
            # 状态，表示当前是第几块石头，是走几步走过来的。
            if i == stones[-1]:
                return True

            # 选择， 走 step + 1 步， 走 step 步，还是走step - 1 步？，
            # 只要往前走的步数有石头（在数组内），就试着可以往前走
            if i + step + 1 in stonesSet:
                if helper(i + step + 1, step + 1):
                    return True

            if i + step in stonesSet:
                if helper(i+ step, step):
                    return True

            if step - 1 > 0 and i + step - 1 in stonesSet:
                #这边要检查一下，step -1 要大于0 才走
                if helper(i+ step - 1, step -1):
                    return True

            return False

        return helper(stones[1], stones[1] - stones[0])

# 动态规划
class Solution:
    def canCross(self, stones) -> bool:
        new_stone = set(stones)
        dp = collections.defaultdict(set)
        dp[0] = {0}
        for num in new_stone:
            for step in dp[num]:
                for i in [step-1, step, step+1]:
                    if i>0 and num+i in new_stone:
                        dp[num+i].add(i)
        return len(dp[stones[-1]]) > 0
