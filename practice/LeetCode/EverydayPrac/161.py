# 773. Sliding Puzzle
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
#
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
#
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
#
# Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
#
# Examples:
#
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1

# Explanation: Swap the 0 and the 5 in one move.

# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.

# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.

# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14

# 方法一：广度优先搜索

class Solution:
    NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 枚举 status 通过一次交换操作得到的状态
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            x = s.index("0")
            for y in Solution.NEIGHBORS[x]:
                s[x], s[y] = s[y], s[x]
                yield "".join(s)
                s[x], s[y] = s[y], s[x]

        initial = "".join(str(num) for num in sum(board, []))
        if initial == "123450":
            return 0

        q = deque([(initial, 0)])
        seen = {initial}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen:
                    if next_status == "123450":
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)

        return -1
