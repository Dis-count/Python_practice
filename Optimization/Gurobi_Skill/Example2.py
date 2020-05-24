# 《数学模型》姜启源第五版 P120 复习题
import gurobipy

# 创建模型
MODEL = gurobipy.Model()

# 创建变量
x1 = MODEL.addVar(vtype=gurobipy.GRB.INTEGER, name='x1')
x2 = MODEL.addVar(ub=3, vtype=gurobipy.GRB.INTEGER, name='x2')
x1_ = MODEL.addVars(range(1, 3), vtype=gurobipy.GRB.INTEGER, name='x1_')
x2_ = MODEL.addVars(range(1, 6), vtype=gurobipy.GRB.INTEGER, name='x2_')
# 更新变量环境
MODEL.update()

# 创建目标函数
MODEL.setObjective(100 * x1 + 40 * x2, sense=gurobipy.GRB.MINIMIZE)

# 创建约束条件
MODEL.addConstr(x1 + x2_[1] >= 4, name='9:00-10:00')
MODEL.addConstr(x1 + x2_[1] + x2_[2] >= 3, name='10:00-11:00')
MODEL.addConstr(x1 + x2_[1] + x2_[2] + x2_[3] >= 4, name='11:00-12:00')
MODEL.addConstr(x1_[1] + x2_[1] + x2_[2] + x2_[3] + x2_[4]>= 6, name='12:00-13:00')
MODEL.addConstr(x1_[2] + x2_[2] + x2_[3] + x2_[4] + x2_[5]>= 5, name='13:00-14:00')
MODEL.addConstr(x1 + x2_[3] + x2_[4] + x2_[5]>= 6, name='14:00-15:00')
MODEL.addConstr(x1 + x2_[4] + x2_[5] >= 8, name='15:00-16:00')
MODEL.addConstr(x1 + x2_[5]>= 8, name='16:00-17:00')

# 此处, sum(x1_) 和 x1_.sum() 结果不同, 因为 sum(x1_) 对字典进行键相加
MODEL.addConstr(x1_.sum() == x1, name='x1')
MODEL.addConstr(x2_.sum() == x2, name='x2')

# 执行最优化
MODEL.optimize()
