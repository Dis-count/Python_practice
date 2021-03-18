# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]

class Solution(object):
    def generateMatrix(self, n):
        if n == 0: return []
        res = [[0] * n for i in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        x, y = 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        count = 0
        while count != n * n:
            res[x][y] = count + 1
            count += 1
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res

# 使用非 0 数字标记边界

class Solution(object):
    def generateMatrix(self, n):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[0] * n for i in range(n)]
        x, y = 0, 0
        count = 0
        cur_d = 0
        while count != n * n:
            res[x][y] = count + 1
            count += 1
            dx, dy = directions[cur_d][0], directions[cur_d][1]
            newx, newy = x + dx, y + dy
            if newx < 0 or newx >= n or newy < 0 or newy >= n or res[newx][newy] != 0:
                cur_d = (cur_d + 1) % 4
                dx, dy = directions[cur_d][0], directions[cur_d][1]
            x, y = x + dx, y + dy
        return res
