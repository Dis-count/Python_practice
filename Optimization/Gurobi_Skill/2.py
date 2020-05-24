import gurobipy
# 1. multidict()
# 扩展字典，便于处理同一个对象的不同属性约束。

EMPLOYEE, MIN, MAX, COST, START, END = gurobipy.multidict({
	"SMITH"   : [6, 8, 30, 6, 20], "JOHNSON": [6, 8, 50, 0, 24], 'WILLIAMS': [6, 8, 30, 0, 24],
	'JONES'   : [6, 8, 30, 0, 24], 'BROWN': [6, 8, 40, 0, 24], 'DAVIS': [6, 8, 50, 0, 24],
	'MILLER'  : [6, 8, 45, 6, 18], 'WILSON': [6, 8, 30, 0, 24], 'MOORE': [6, 8, 35, 0, 24],
	'TAYLOR'  : [6, 8, 40, 0, 24], 'ANDERSON': [2, 3, 60, 0, 6], 'THOMAS': [2, 4, 40, 0, 24],
	'JACKSON' : [2, 4, 60, 8, 16], 'WHITE': [2, 6, 55, 0, 24], 'HARRIS': [2, 6, 45, 0, 24],
	'MARTIN'  : [2, 3, 40, 0, 24], 'THOMPSON': [2, 5, 50, 12, 24], 'GARCIA': [2, 4, 50, 0, 24],
	'MARTINEZ': [2, 4, 40, 0, 24], 'ROBINSON': [2, 5, 50, 0, 24]})

# 2. tuplelist()
# 扩展列表元组，可以使用通配符筛选变量组。若使用 tuplelist 创建变量：

Cities= [('A','B'), ('A','C'), ('B','C'),('B','D'),('C','D')]
Routes = gurobipy.tuplelist(Cities)

Routes.select('A','*') # 选出所有第一个, 素为 "A" 的, 组

# 此外, 对于addVars创建的变量, x.select("*", i, j) 也可以进行筛选(详见案例3.6)

# 可以将 '*' 理解为切片操作(列表的 list[:])


# 3. prod() 和 sum() 下标聚合

gurobipy.quicksum(cost[i,j] * x[i,j] for i,j in arcs)
# 等价于 x.prod(cost)
# 效果为对应元素相乘再相加
