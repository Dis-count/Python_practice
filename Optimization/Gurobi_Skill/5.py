# 非平衡指派问题
# C=c_ij n,m

import gurobipy

def assignment(cost_matrix):
	# 保存行列标签
	index = cost_matrix.index
	columns = cost_matrix.columns

	# 创建模型
	model = gurobipy.Model('Assignment')
	x = model.addVars(index, columns, vtype=gurobipy.GRB.BINARY)
	model.update()

	# 设置目标函数
	model.setObjective(gurobipy.quicksum(x[i, j] * cost_matrix.at[i, j] for i in index for j in columns))

	# 添加约束条件
	model.addConstr(gurobipy.quicksum(x[i, j] for i in index for j in columns) == min([len(index), len(columns)]))
	model.addConstrs(gurobipy.quicksum(x[i, j] for j in columns) <= 1 for i in index)
	model.addConstrs(gurobipy.quicksum(x[i, j] for i in index) <= 1 for j in columns)

	# 执行最优化
	model.optimize()

	# 输出信息
	result = cost_matrix * 0
	if model.status == gurobipy.GRB.Status.OPTIMAL:
		solution = [k for k, v in model.getAttr('x', x).items() if v == 1]
		for i, j in solution:
			print(f"{i} -> {j}：{cost_matrix.at[i,j]}")
			result.at[i, j] = 1
	return result


if __name__ == '__main__':
	import pandas as pd

	cost_matrix = pd.DataFrame(
			[[4, 8, 7, 15, 12], [7, 9, 17, 14, 10], [6, 9, 12, 8, 7], [6, 7, 14, 6, 10], [6, 9, 12, 10, 6],
				[5, 8, 13, 11, 10]],
			index=['A1', 'A2', 'A3', 'A4', 'A5', 'A6'], columns=['B1', 'B2', 'B3', 'B4', 'B5'])

	assignment(cost_matrix)


# 在 scipy 模块中，也有 linear_sum_assignment 函数可以求解指派问题，使用的是匈牙利算法，虽然求解速度也很快，但对于数据要求比较苛刻（矩阵不能太大，大型矩阵需要先进行稀疏处理）

def zeros_ones_integer_programmingg(cost_matrix):
    import numpy as np
    from scipy.optimize import linear_sum_assignment
    solution_matrix = np.zeros_like(cost_matrix)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    solution_matrix[row_ind, col_ind] = 1
    minimize = (cost_matrix*solution_matrix).sum()
    if type(cost_matrix) == pd.core.frame.DataFrame:
        solution_matrix = pd.DataFrame(solution_matrix, index = cost_matrix.index,columns= cost_matrix.columns)
        minimize = minimize.sum()
    return solution_matrix,minimize

if __name__ == '__main__':
    import numpy as np
    cost_matrix = np.array([[2, 15, 13, 4], [10, 4, 14, 15], [9, 14, 16, 13], [7, 8, 11, 9]])   # 代价矩阵
    print(zeros_ones_integer_programmingg(cost_matrix))
