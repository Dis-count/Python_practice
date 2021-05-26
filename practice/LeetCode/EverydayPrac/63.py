# 407. Trapping Rain Water II
# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.
#
# Example:
#
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
#
# Return 4.

# 解题思路  堆 + BFS
# 一个木桶的接水数量取决于木桶的最短边高度。
# 用最小堆存储木桶各边的高度，每次弹出最短的边，它只决定与其相邻的柱子可以存水的量。

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = set()
        heap = []
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited.add((i, 0))
            visited.add((i, n-1))
        for j in range(1, n-1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited.add((0, j))
            visited.add((m-1, j))

        ans = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                    near_h = heightMap[new_i][new_j]
                    if near_h < h:
                        ans += h - near_h
                    heapq.heappush(heap, (max(h, near_h), new_i, new_j))
                    visited.add((new_i, new_j))
        return ans

# 时间复杂度：O(MN * log (M+N))，每个柱子操作一次，共MN个柱子，堆操作是log级，堆中元素最多为2M+2N（即桶的边数）。
# 空间复杂度：O(MN)。
