# 创建多个变量

x = MODEL.addVars(3, 4, 5, vtype=gurobipy.GRB.BINARY, name="C") # 创建 3*4*5 个变量，使用 x[1,2,3] 进行访问
# lb，ub，vtype 可以单独设置(同样维度数据)，也可以全部设置(单个值)
# 此外，若使用 m.addVars(iterable1,iterable2,iterable3) ，相当于笛卡尔积，参考案例 4.2
# 这种创建方法可以使用通配符命令，能简化代码

# 添加完变量后需要 MODEL.update() 更新变量空间

# 多目标优化（默认最小）

# expression: 表达式，可以是一次或二次函数类型
# index: 目标函数对应的序号 (默认 0，1，2，…), 以 index=0 作为目标函数的值, 其余值需要另外设置参数
# priority: 分层序列法多目标决策优先级(整数值), 值越大优先级越高
# weight: 线性加权多目标决策权重(在优先级相同时发挥作用)
# abstol: 分层序列法多目标决策时允许的目标函数值最大的降低量
# reltol: 分层序列法多目标决策时允许的目标函数值最大的降低比率 reltol*|目标函数值|

# 1. 合成型 ######################################################
# Obj1 = x + y          weight = 1
# Obj2 = x - 5 * y      weight = -2
# MODEL.setObjectiveN(x + y, index=0, weight=1, name='obj1')
# MODEL.setObjectiveN(x -5 * y, index=1, weight=-2, name='obj2')
# 即转化为：(x + y) - 2 * (x - 5 * y) = - x + 11 * y
​
# 2. 分层优化型(目标约束时使用) #####################################
# Obj1 = x + y          priority = 5
# Obj2 = x - 5 * y      priority = 1
# MODEL.setObjectiveN(x + y, index=0, priority=5, name='obj1')
# MODEL.setObjectiveN(x -5 * y, index=1, priority=1, name='obj2')
# 即转化为：先优化 Obj1，再优化 Obj2（按照 priority 的大小关系）
  ​
# 3. 混合优化型 ##################################################
# MODEL.setObjectiveN(x + y, index=0, weight=1, priority=5, name='obj1')
# MODEL.setObjectiveN(x -5 * y, index=1, weight=-2, priority=1, name='obj2')
# 则 先优化 Obj1 再优化 Obj2 最后相加作为目标值
  ​
# 4. 执行最优化结束后，获取目标函数值  ###############################
# MODEL.setParam(gurobipy.GRB.Param.ObjNumber, i)   # 第 i 个目标
# print(MODEL.ObjNVal)  # 打印第 i 个值


# 分段目标
# MODEL.setPWLObj(var, x, y)

# var 指定变量的目标函数是分段线性
# x 定义分段线性目标函数的点的横坐标值(非减序列)
# y 定义分段线性目标函数的点的纵坐标值

MODEL.setPWLObj(x, [0, 2, 5], [0, 2, 3])
MODEL.setAttr(gurobipy.GRB.Attr.ModelSense, -1)


# 添加约束
MODEL.addConstr(expression, name="")
#
# expression: 布尔表达式，可以是一次或二次函数类型
# name: 约束式的名称

MODEL.addConstr(12 * x1 + 9 * x2 + 25 * x3 + 20 * x4 + 17 * x5 + 13 * x6 >= 60, "c0")
# 注意，此处是调用 c 库实现的，若有 a < b < c，只能拆开写成 a < b，和 b < c

x = MODEL.addVars(20, 8, vtype=gurobipy.GRB.BINARY)
# 写法 1
for i in range(20):
    MODEL.addConstr(x.sum(i, "*") <= 1)
# 写法 2
MODEL.addConstrs(x.sum(i, "*") <= 1 for i in range(20))


# 创建一个范围约束
MODEL.addRange(expression, min_value, max_value, name="")

# 表达式 min_value<=expression<=max_value 的简写, 但这里的 min_value, max_value 必须是具体的实数值, 不能含有变量

# 创建指示变量

# 案例: 如果生产某一类型汽车 (x[i] > 0), 则至少要生产 80 辆
# %% 方法一
for i in range(3):
	MODEL.addGenConstrIndicator(y[i + 1], 1, x[i + 1] >= 80)
	MODEL.addGenConstrIndicator(y[i + 1], 0, x[i + 1] == 0)

# 以上代码等价于
for i in range(3):
	MODEL.addConstr(x[i + 1] >= 80 * y[i + 1])
	MODEL.addConstr(x[i + 1] <= 1000 * y[i + 1])


# 执行最优化
MODEL.Params.LogToConsole=True # 显示求解过程
MODEL.Params.MIPGap=0.0001 # 百分比界差
MODEL.Params.TimeLimit=100 # 限制求解时间为 100s

MODEL.optimize()

# 查看状态
MODEL.status == gurobipy.GRB.Status.OPTIMAL


# 查看目标函数值
print("Optimal Objective Value", MODEL.objVal)
# 查看多目标规划模型的目标函数值
for i in range(MODEL.NumObj):
	MODEL.setParam(gurobipy.GRB.Param.ObjNumber, i)
	print(f"Obj {i+1} = {MODEL.ObjNVal}")


# 查看变量取值
for var in MODEL.getVars():
   print(f"{var.varName}: {round(var.X, 3)}")


# 灵敏度分析
通过 MODEL.getVars() 得到的变量 var

使用 var.X 可以获取变量值, var.RC 可以获取 Reduced Cost；
var.Obj 可以得到在目标函数中的系数
var.SAObjLow 可以得到 Allowable Minimize
var.SAObjUp 可以得到 Allowable Maximize
通过 MODEL.getConstrs() 得到的约束式 Constr

Constr.Slack 可以得到 Slack or Surplus
Constr.pi 可以得到 Dual Price
Constr.RHS 可以得到约束式右侧常值
Constr.SARHSLow 可以得到 Allowable Minimize
Constr.SARHSUp 可以得到 Allowable Maximize
