# 解数独

# 数独问题就是将 9 × 9 的网格填充上1~9的整数值，同时保证每个整数在每一行、每一列和每个 3 × 3 方格只出现一次。网格中分布有一些线索，你的任务就是填充剩余的网格数字。对于此问题，可以使用0-1变量优化求解。

# 标准数独问题只要有解即可，无需设置目标函数，即：可行解就是数独问题的解。

# x_ijk =1 if 第i行,第j列值为k, =0 else

# 约束条件
# 1.对于给定的初始元素，都认为是等式约束：
# 2. 所有格子只能取一个值，对k 加和为1.
# 3. 每个数字在同一行、同一列、同一个九宫格只能出现一次： 三个约束

import gurobipy
import pandas as pd

def sudoku(matrix):
	MODEL = gurobipy.Model('solve_sudoku')
	x = MODEL.addVars(9, 9, 9, vtype=gurobipy.GRB.BINARY)
	MODEL.update()
	MODEL.setObjective(1, gurobipy.GRB.MINIMIZE)

	MODEL.addConstrs(x[i, j, k] == 1 for i in range(9) for j in range(9) for k in range(9) if isinstance(matrix.at[i, j], int) and k == matrix.at[i, j] - 1)
	MODEL.addConstrs(sum(x.select(i, j, '*')) == 1 for i in range(9) for j in range(9))
	MODEL.addConstrs(sum(x.select(i, '*', j)) == 1 for i in range(9) for j in range(9))
	MODEL.addConstrs(sum(x.select('*', i, j)) == 1 for i in range(9) for j in range(9))
	MODEL.addConstrs(sum(x[i + 3 * I, j + 3 * J, k] for i in range(3) for j in range(3)) == 1 for k in range(9) for I in range(3) for J in range(3))

	MODEL.optimize()
	Result = pd.DataFrame()
	for k, v in MODEL.getAttr('x', x).items():
		if v == 1:
			Result.at[k[0], k[1]] = k[2] + 1
	return Result.astype(int)


if __name__ == '__main__':
	matrix = pd.read_excel('sudoku_test.xlsx', index_col=False, header=None, na_filter=False)
	print(sudoku(matrix))
t(sudoku(matrix))
