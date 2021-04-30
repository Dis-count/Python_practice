
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

# 递归

class Solution:
    def canCross(self, stones) -> bool:
        if stones[1] - stones[0] > 1: return False
        end = stones[-1]
        @functools.lru_cache(None)
        def helper(step, idx):
            if idx == end:
                return True
            for step_new in (step-1, step, step+1):
                if step_new <= 0:
                    continue
                else:
                    if step_new+idx in stones and helper(step_new, step_new+idx)==True:
                        return True
            return False
        return helper(1,1)
