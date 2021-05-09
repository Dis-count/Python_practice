# 1723. Find Minimum Time to Finish All Jobs
# You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.
#
# There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.
#
# Return the minimum possible maximum working time of any assignment.
#
# Example 1:
#
# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.
#
# Example 2:
#
# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11.


# 最小最大完工时间 显然是一个 NP-hard 问题
# 因此 可以考虑 用 二分回溯 在每个 limit 遍历可行方案 找到 min limit 即可。
# 动态规划 状态压缩 但状态 显然指数个
#  回溯 结合 剪枝操作（先试大的 job time, 尽量优先分配任务给未分配任务的人）
#  模拟退火算法

# import math
# math.factorial(4)
# 2**10
# 显然 阶乘远大于指数

from typing import List
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        def check(limit):
            # 剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快
            arr = sorted(jobs)

            groups = [0] * k
            # 分成 K 组，看看在这个limit 下 能不能安排完工作
            if backtrace(arr, groups, limit):
                return True
            else:
                return False

        def backtrace(arr, groups, limit):
            # 尝试每种可能性
            #print(arr, groups, limit)
            if not arr: return True #分完，则方案可行
            v = arr.pop()

            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v

                    # 如果这个工人分活失败（给他分配这个任务后所有的尝试都是失败的），则剪枝，因为也没必要再往后试了，其他人也会出现一样的情况
                    if groups[i] == 0:
                        break

            arr.append(v)

            return False

        #每个人承担的工作的上限，最小为，job 里面的最大值，最大为 jobs 之和
        l, r  = max(jobs), sum(jobs)

        while l < r:
            mid = (l + r)//2

            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l
