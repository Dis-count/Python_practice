from gurobipy import *
m =Model()
v0 = m.addVar()
v1 = m.addVar()
m.update()
m.addConstr(v0 - v1 <= 4) # Constraint 1
m.addConstr(v0 + v1 <= 4) # Constraint 2
m.addConstr(-0.25*v0 + v1 <= 1) # Constraint 3
m.setObjective(v1, GRB.MAXIMIZE) # Objective: maximize v1
m.params.outputflag = 0
m.optimize()

# 用于画线段
import matplotlib.pyplot as pyplot
pyplot.plot([0,4], [0,4]) # Constraint 1  先写x 后写y坐标
pyplot.plot([4,0], [0,4]) # Constraint 2
pyplot.plot([0,4], [1,2]) # Constraint 3
pyplot.plot([v0.x], [v1.x], 'ro') # Plot the optimal vertex
pyplot.show()

####################################################
# 在一张图上画多条曲线
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)  #设置横轴的取值点

y1 = 2 * x + 1
#曲线1
y2 = x**2
#曲线2
plt.figure(num=3,figsize=(8,5))  #  设置坐标轴的长度

plt.title('Result Analysis')
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1,label='y1',linestyle='--',marker='*')
# 设置坐标轴的取值范围
plt.xlim((-1,2))
plt.ylim((-1,2))
# 设置坐标轴的名称
plt.xlabel('XXX')
plt.ylabel('YYY')
# 图例
plt.legend()
# 重新设置坐标轴上的刻度
new_ticks = np.linspace(-1,2,10)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],['really bad','bad','normal','good','really good'])

plt.show()
