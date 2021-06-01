# 1882. 使用服务器处理任务
# 给你两个 下标从 0 开始 的整数数组 servers 和 tasks ，长度分别为 n​​​​​​ 和 m​​​​​​ 。servers[i] 是第 i​​​​​​​​​​ 台服务器的 权重 ，而 tasks[j] 是处理第 j​​​​​​ 项任务 所需要的时间（单位：秒）。
#
# 你正在运行一个仿真系统，在处理完所有任务后，该系统将会关闭。每台服务器只能同时处理一项任务。第 0 项任务在第 0 秒可以开始处理，相应地，第 j 项任务在第 j 秒可以开始处理。处理第 j 项任务时，你需要为它分配一台 权重最小 的空闲服务器。如果存在多台相同权重的空闲服务器，请选择 下标最小 的服务器。如果一台空闲服务器在第 t 秒分配到第 j 项任务，那么在 t + tasks[j] 时它将恢复空闲状态。
#
# 如果没有空闲服务器，则必须等待，直到出现一台空闲服务器，并 尽可能早 地处理剩余任务。 如果有多项任务等待分配，则按照 下标递增 的顺序完成分配。
#
# 如果同一时刻存在多台空闲服务器，可以同时将多项任务分别分配给它们。
#
# 构建长度为 m 的答案数组 ans ，其中 ans[j] 是第 j 项任务分配的服务器的下标。
#
# 返回答案数组 ans​​​​ 。
#
# 示例 1：
#
# 输入：servers = [3,3,2], tasks = [1,2,3,2,1,2]
# 输出：[2,2,0,2,1,2]
# 解释：事件按时间顺序如下：
# - 0 秒时，第 0 项任务加入到任务队列，使用第 2 台服务器处理到 1 秒。
# - 1 秒时，第 2 台服务器空闲，第 1 项任务加入到任务队列，使用第 2 台服务器处理到 3 秒。
# - 2 秒时，第 2 项任务加入到任务队列，使用第 0 台服务器处理到 5 秒。
# - 3 秒时，第 2 台服务器空闲，第 3 项任务加入到任务队列，使用第 2 台服务器处理到 5 秒。
# - 4 秒时，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 5 秒。
# - 5 秒时，所有服务器都空闲，第 5 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。
#
# 示例 2：
#
# 输入：servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
# 输出：[1,4,1,4,1,3,2]
# 解释：事件按时间顺序如下：
# - 0 秒时，第 0 项任务加入到任务队列，使用第 1 台服务器处理到 2 秒。
# - 1 秒时，第 1 项任务加入到任务队列，使用第 4 台服务器处理到 2 秒。
# - 2 秒时，第 1 台和第 4 台服务器空闲，第 2 项任务加入到任务队列，使用第 1 台服务器处理到 4 秒。
# - 3 秒时，第 3 项任务加入到任务队列，使用第 4 台服务器处理到 7 秒。
# - 4 秒时，第 1 台服务器空闲，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 9 秒。
# - 5 秒时，第 5 项任务加入到任务队列，使用第 3 台服务器处理到 7 秒。
# - 6 秒时，第 6 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。

# 因此，我们就可以设计出算法的流程：
#
# 在初始时，我们将所有服务器放入优先队列 idle 中，并使用一个时间戳变量 ts 记录当前的时间，其初始值为 0；
#
# 随后我们遍历每一个任务：
#
# 由于第 i 个任务必须在时间 i 时才可以开始，因此需要将 ts 置为其与 i 的较大值；
#
# 我们需要将优先队列 busy 中满足 t≤ts 的服务器依次取出并放入优先队列 idle；
#
# 如果此时优先队列 idle 中没有服务器，说明我们需要等一台服务器完成任务，因此可以将 ts 置为优先队列 busy 的队首服务器的任务完成时间 t，并再次执行上一步；
#
# 此时我们就可以给第 i 个任务安排服务器了，即为优先队列 idle 的队首服务器，将其取出并放入优先队列 busy。

from typing import List
import heapq

#  Have a test
# heap = [4,3,5]
# heapq.heapify(heap)
# heapq.heappop(heap)

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # 工作中的服务器，存储二元组 (t, idx) t 结束时间
        busy = list()

        # 空闲的服务器，存储二元组 (w, idx) w is weight
        idle = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(idle)

        ts = 0
        # 将优先队列 busy 中满足 t<=ts 依次取出并放入优先队列 idle
        def release():
            while busy and busy[0][0] <= ts:
                _, idx = heapq.heappop(busy)
                heapq.heappush(idle, (servers[idx], idx))

        ans = list()
        for i, task in enumerate(tasks):
            ts = max(ts, i)
            release()
            if not idle:
                ts = busy[0][0]
                release()

            _, idx = heapq.heappop(idle)
            ans.append(idx)
            heapq.heappush(busy, (ts + task, idx))

        return ans
