# 利用整数线性规划最优化员工工作表

# (1) 问题描述

# 下图分别为员工信息（包含每日最短工作时长、最长工作时长、单位小时工作薪资、可工作时间）、每小时最短工作人数，要求满足以下条件：

#满足每小时最短工作人数
#如果员工进行工作，则需满足个人工作时长不低于最小值、不高于最大值
#每位员工每天至多工作一个班次，每个班次都是一段连续的时间
#请给出一种分配方案，使得每日支付员工的薪水最少。

import gurobipy

# 创建模型
EMPLOYEE, MIN, MAX, COST, START, END = gurobipy.multidict({
	"SMITH"   : [6, 8, 30, 6, 20], "JOHNSON": [6, 8, 50, 0, 24], 'WILLIAMS': [6, 8, 30, 0, 24],
	'JONES'   : [6, 8, 30, 0, 24], 'BROWN': [6, 8, 40, 0, 24], 'DAVIS': [6, 8, 50, 0, 24],
	'MILLER'  : [6, 8, 45, 6, 18], 'WILSON': [6, 8, 30, 0, 24], 'MOORE': [6, 8, 35, 0, 24],
	'TAYLOR'  : [6, 8, 40, 0, 24], 'ANDERSON': [2, 3, 60, 0, 6], 'THOMAS': [2, 4, 40, 0, 24],
	'JACKSON' : [2, 4, 60, 8, 16], 'WHITE': [2, 6, 55, 0, 24], 'HARRIS': [2, 6, 45, 0, 24],
	'MARTIN'  : [2, 3, 40, 0, 24], 'THOMPSON': [2, 5, 50, 12, 24], 'GARCIA': [2, 4, 50, 0, 24],
	'MARTINEZ': [2, 4, 40, 0, 24], 'ROBINSON': [2, 5, 50, 0, 24]})

REQUIRED = [1, 1, 2, 3, 6, 6, 7, 8, 9, 8, 8, 8, 7, 6, 6, 5, 5, 4, 4, 3, 2, 2, 2, 2]

MODEL = gurobipy.Model("Work Schedule")

# 创建变量
x = MODEL.addVars(EMPLOYEE, range(24), range(1, 25), vtype=gurobipy.GRB.BINARY)

# 更新变量环境
MODEL.update()

# 创建目标函数
MODEL.setObjective(gurobipy.quicksum((j - i) * x[d, i, j] * COST[d] for d in EMPLOYEE for i in range(24) for j in range(i + 1, 25)), sense=gurobipy.GRB.MINIMIZE)

# 创建约束条件
MODEL.addConstrs(x.sum(d) <= (gurobipy.quicksum(x[d, i, j] for i in range(START[d], END[d] + 1) for j in range(i + 1, END[d] + 1) if MIN[d] <= j - i <= MAX[d])) for d in EMPLOYEE)
MODEL.addConstrs(gurobipy.quicksum(x[d, i, j] for i in range(START[d], END[d] + 1) for j in range(i + 1,END[d] + 1) if MIN[d] <= j - i <= MAX[d]) <= 1 for d in EMPLOYEE)
MODEL.addConstrs(gurobipy.quicksum(x[d, i, j] for d in EMPLOYEE for i in range(24) for j in range(i + 1, 25) if i <= c < j) >= REQUIRED[c] for c in range(24))

# 执行最优化
MODEL.optimize()

# 输出结果 —— 使用pyecharts
from pyecharts import HeatMap
x_axis = list(range(24))
y_axis = []
data = []
if MODEL.status == gurobipy.GRB.Status.OPTIMAL:
	solution = [k for k, v in MODEL.getAttr('x', x).items() if v == 1]
	for d, i, j in solution:
		print(f"The working time of {d} is from {i} to {j}")
		y_axis.append(d)
		data.extend([[time, d, COST[d]] for time in range(i, j)])
	for c in range(24):
		member = [d for d, i, j in solution if i <= c < j]
		print(f'The member of staff from {c} -{c+1}: {",".join(member)}')

def label_formatter(param):
	return param.x
def yaxis_formatter(param):
	return param

heatmap = HeatMap(width=1100, height=500)
heatmap.add("", x_axis, y_axis, data, is_visualmap=True, visual_text_color="#000", visual_orient="horizontal", visual_pos="center", visual_range=[30, 50], is_calculable=False, is_label_show=True, label_formatter=label_formatter, yaxis_formatter=yaxis_formatter, label_pos="inside")
heatmap.render("result.png")
