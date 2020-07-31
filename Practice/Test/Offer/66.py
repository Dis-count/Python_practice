# 机器人运动范围
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如
# a & b & c & e \\
# s & f & c & s \\
# a & d & e & e \\
# 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

# 分析：回溯算法
#  这是一个可以用回朔法解决的典型题。首先，在矩阵中任选一个格子作为路径的起点。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的
# 第i个位置。如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子之外，其他格子都有4个相邻的格子。
# 重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。
# 　　由于回朔法的递归特性，路径可以被开成一个栈。当在矩阵中定位了路径中前n个字符的位置之后，在与第n个字符对应的格子的周围都没有找到第n+1个
# 字符，这个时候只要在路径上回到第n-1个字符，重新定位第n个字符。
# 　　由于路径不能重复进入矩阵的格子，还需要定义和字符矩阵大小一样的布尔值矩阵，用来标识路径是否已经进入每个格子。 当矩阵中坐标为（row,col）的
# 格子和路径字符串中相应的字符一样时，从4个相邻的格子(row,col-1),(row-1,col),(row,col+1)以及(row+1,col)中去定位路径字符串中下一个字符
# 如果4个相邻的格子都没有匹配字符串中下一个的字符，表明当前路径字符串中字符在矩阵中的定位不正确，我们需要回到前一个，然后重新定位。
# 　　一直重复这个过程，直到路径字符串上所有字符都在矩阵中找到合适的位置

# 用递归来实现DFS
# 1.确定出口：
# false:1.边界条件不满足，2.当前字符不匹配，3.已经遍历过
# true：字符串str已经遍历结束
# 2.递：设置访问过
# 递归方式，按照上下左右递归
# 3.归：复位，未访问

# -*- coding:utf-8 -*-
#回溯法
#遍历矩阵中的每一个位置
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.exist_helper(x, i, j, path):
                    return True
        return False
    def exist_helper(self, matrix, i, j, p):  # p 为给定path
        if  matrix[i][j] == p[0]:
            if not p[1:]:
                return True
            matrix[i][j] = ''
            if i > 0 and self.exist_helper(matrix, i-1, j, p[1:]):  # 左
                return True
            if i < len(matrix)-1 and self.exist_helper(matrix, i+1, j ,p[1:]): #右
                return True
            if j > 0 and self.exist_helper(matrix, i, j-1, p[1:]): # 下
                return True
            if j < len(matrix[0])-1 and self.exist_helper(matrix, i, j+1, p[1:]):# 上
                return True
            matrix[i][j] = p[0]
            return False
        else:
            return False


# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, board, row, col, word):
        self.col, self.row = col, row
        board = [list(board[col * i:col * i + col]) for i in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    self.b = False
                    self.search(board, word[1:], [(i, j)], i, j)
                    if self.b:
                        return True

        return False

    def search(self, board, word, dict, i, j):
        if word == "":
            self.b = True
            return
        if j != 0 and (i, j - 1) not in dict and board[i][j - 1] == word[0]:
            self.search(board, word[1:], dict + [(i, j - 1)], i, j - 1)
        if i != 0 and (i - 1, j) not in dict and board[i - 1][j] == word[0]:
            self.search(board, word[1:], dict + [(i - 1, j)], i - 1, j)
        if j != self.col - 1 and (i, j + 1) not in dict and board[i][j + 1] == word[0]:
            self.search(board, word[1:], dict + [(i, j + 1)], i, j + 1)
        if i != self.row - 1 and (i + 1, j) not in dict and board[i + 1][j] == word[0]:
            self.search(board, word[1:], dict + [(i + 1, j)], i + 1, j)
