# 279. Perfect Squares
# Given an integer n, return the least number of perfect square numbers that sum to n.
#
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# M1 BFS
# 以初始值 n 为起点开始向外扩张，直到找到一个完全平方数就返回答案。答案存在cache（或者visit数组）中，每扩张一次 +1
class Solution:
    def numSquares(self, n: int) -> int:
        ps = [i * i for i in range(1, int(n**0.5)+1)][::-1] # 从大到小减去，帮助加速
        pset = set(ps)
        queue, cache = [n], {n:1}
        while queue:
            val = queue.pop(0)
            if val in pset: return cache[val]
            for p in ps:
                if val-p > 0 and val-p not in cache:
                    queue.append(val-p)
                    cache[val-p] = cache[val] + 1
        return -1

n = 26
a = Solution()
a.numSquares(n)

# 完全背包 DP
# 把所有的完全平方数整理出来，然后就变成了一个完全背包问题（因为每个数字可以放无限次）。
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i*i for i in range(1, int(n**0.5)+1)]
        f = [0] + [float('inf')]*n
        for num in nums:
            for j in range(num, n+1):
                f[j] = min(f[j], f[j-num]+1)
        return f[-1]

# 贪心算法
# 类似素数筛选一样，把每一个数字从小到大开始标记。标记的值为“这个数字n能最少是几个完全平方数的和”（也就是数字n的答案）。
class Solution:
    def numSquares(self, n: int) -> int:
        ps = set([i * i for i in range(1, int(n**0.5)+1)])
        def divisible(n, count):
            if count == 1: return n in ps
            for p in ps:
                if divisible(n-p, count-1):
                    return True
            return False

        for count in range(1, n+1):
            if divisible(n, count):
                return count
