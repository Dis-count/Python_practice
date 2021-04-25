# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 0:07
# @Author  : AWAYASAWAY
# @File    : 校车路径优化.py
# @IDE     : PyCharm

import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import copy
import math
import sys

# 字体设置
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']

# 规定每辆车的承载能力，假设每个学生占据的空间为 1
bus_capaticy = 20
qc = 1
# 学校上课时间，设置为早上8：00，假设为480
rolling_time = 480
# 车辆行驶速度，假设为6个单位每分钟
velocity = 6
# 学校/中转站
school_location = [[35, 35]]
# 学生位置坐标
student_location = []
StuLocation = []
with open(r'学生位置坐标.txt') as f:
    for line in f:
        # 将所有点的位置坐标储存在location中
        StuLocation.append(list(line.strip('\n').split(',')))
    for i in range(len(StuLocation)):
        x = float(StuLocation[i][0])
        y = float(StuLocation[i][1])
        student_location.append([x, y])
# 所有的位置坐标location
location = student_location + school_location
# 长度location
n = len(location)
# 校车在各个位置之间行驶所需的时间
# 距离矩阵 == 花费的时间矩阵
distance = [[0 for col in range(n)] for raw in range(n)]
for i in range(n):
    for j in range(n):
        x = pow(location[i][0] - location[j][0], 2)
        y = pow(location[i][1] - location[j][1], 2)
        distance[i][j] = pow(x + y, 0.5) / velocity
# 学校到各个家庭之间的距离 == 行驶的时间
schooltohome = distance[0]
# 构建学校和家庭之间的距离字典，键：编号；值：[对应的学生家庭坐标，学校和该家庭之间的距离]
# 0号表示学校
shdic = {}
stohome = []  # [[对应的距离，编号], ..., [] ]
for i in range(len(schooltohome)):
    shdic[i] = [location[i], schooltohome[i]]
    stohome.append([schooltohome[i], i])
# 将学校到学生家庭住址的距离安照降序排列
school_to_home = copy.copy(schooltohome)
school_to_home.sort(reverse=True)
# 移除0元素，即学校到学校
school_to_home.remove(school_to_home[-1])
# 将排列好的距离换成家庭住址的编号
for i in range(len(school_to_home)):
    for j in range(len(stohome)):
        if stohome[j][0] == school_to_home[i]:
            school_to_home[i] = stohome[j][1]
            stohome[j][0] = '已使用'


# -------------- 计算校车走完路径route所需的时间 -------------- #
def calc_time(route):
    route_time = 0
    for i in range(len(route) - 1):
        route_time += distance[route[i]][route[i + 1]]
    return rolling_time


# -------------- 插入算法，u为路径，v为待插入点 -------------- #
def insertnode(u, v):
    if len(u) == 0:  # 若路径长度为0，直接插入节点
        finalroute = [v]
    else:  # 若路径长度不为0，插入节点v，节点v的插入后使路径长度 增加值 最小
        candidate_route = [[0 for col in range(len(u) + 1)] for row in range(len(u) + 1)]
        for i in range(len(u)):
            u2 = copy.deepcopy(u)  # 深拷贝
            u2.insert(i, v)
            candidate_route[i] = u2
            # print(candidate_route)
        u3 = copy.deepcopy(u)
        u3.append(v)
        candidate_route[-1] = u3
        # print(candidate_route)
        candidate_routecost = [calc_time(route) for route in candidate_route]
        # print(candidate_routecost)
        min_routecost = min(candidate_routecost)
        min_route = candidate_route[candidate_routecost.index(min_routecost)]
        finalroute = min_route
    return finalroute


# -------------- 链生产算法，只考虑了一个学校，省略了school loop -------------- #
def buildchains():
    bus_used = []  # 车辆行驶的路径，其中每个子列表代表一辆车的行驶路径
    b = 0
    occb = 0
    bus_route = []
    home = copy.copy(school_to_home)
    # print(home)
    # 算法迭代逻辑与论文图片逻辑相同
    for i in range(len(home)):
        if occb < bus_capaticy:
            sv = home[i]
            # print(sv)
            bus_route1 = insertnode(bus_route, sv)
            bus_route = bus_route1
            # print(bus_route)
            occb += qc
            if i == len(home) - 1:
                bus_used.append(bus_route)
        else:
            bus_used.append(bus_route)
            b += 1
            occb = 0
            bus_route = []
            sv = home[i]
            # print(sv)
            bus_route1 = insertnode(bus_route, sv)
            bus_route = bus_route1
            occb += qc
            if i == len(home) - 1:
                bus_used.append(bus_route)
    return bus_used


# print(buildchains())
initial_solution = buildchains()
# 假设初始位置和结束位置都为学校，即在initial_solution中的首尾都需要0（学校编号）
for ini in initial_solution:
    ini.append(0)
    ini.insert(0, 0)


# -------------- 禁忌搜索算法，只考虑目标函数F1 -------------- #
def function(solution):
    # 由论文中的公式8,可知需求出公式6的值, Os(c)=480, d\
    f1 = 0
    for i in solution:
        for j in range(1, len(i) - 1):
            equation8_1 = calc_time(i[j:])  # 公式8中括号所表示的值
            # print(equation8_1)
            equation8_2 = distance[0][i[j]]  # 公式8中d(hc-sc)的值，即学校到该地址的时间
            fc = equation8_1 - equation8_2  # 公式8的值，表示第i个solution中第j个元素的fc
            f1 += fc
    return f1


# -------------- 利用禁忌搜索算法对初始解进行优化 -------------- #
def exchange(sol, rand):  # 算子，随机交换两个学生的位置
    s1 = []
    for i in sol:
        for j in i:
            s1.append(j)
    sol = s1
    # print(sol)
    index1 = sol.index(rand[0])
    index2 = sol.index(rand[1])
    sol[index1] = rand[1]
    sol[index2] = rand[0]
    sol1 = sol[0:22]
    sol2 = sol[22:44]
    sol3 = sol[44:]
    solution = [sol1, sol2, sol3]
    return solution


# -------------- 初始设置 -------------- #
tabu_list = []
tabu_time = []
current_tabu_num = 0  # 当前禁忌对象数量
tabu_limit = 50  # 禁忌长度，即禁忌期限
best_route = []
best_distance = sys.maxsize
current_route = []
current_distance = 0.0


# -------------- 初始设置 -------------- #
def setup():
    global best_route
    global best_distance
    global tabu_time
    global current_tabu_num
    global current_route
    global tabu_list
    # 得到初始解以及初始化目标函数
    current_route = initial_solution
    best_route = copy.copy(current_route)
    current_distance = function(current_route)
    best_distance = current_distance
    # 置禁忌表为空
    tabu_list.clear()
    tabu_time.clear()
    current_tabu_num = 0


# -------------- 得到邻域解，候选解 -------------- #
def get_candidate():
    global best_route
    global best_distance
    global current_tabu_num
    global current_distance
    global current_route
    global tabu_list
    iter_solution = []  # 存储此次迭代得到的所有解
    temp = 0
    candidate = [0 for raw in range(100)]  # 候选集
    candidate_distance = [0 for col in range(100)]
    # 随机选取邻域
    while True:
        rand = random.sample(range(1, len(student_location)), 2)
        if rand not in iter_solution:
            iter_solution.append(rand)
            # print(iter_solution)
            # exchan = exchange(current_route, rand)
            # candidate[temp] = operator(current_route, exchan[0], exchan[1], rand)
            candidate[temp] = exchange(current_route, rand)
            if candidate[temp] not in tabu_list:
                candidate_distance[temp] = function(candidate[temp])
                temp += 1
            if temp >= 100:
                break
    # 　得到候选解中的最优解
    candidate_best = min(candidate_distance)
    best_index = candidate_distance.index(candidate_best)
    current_distance = candidate_best
    current_route = copy.copy(candidate[best_index])
    # 与当前最优解进行比较
    if current_distance < best_distance:
        best_distance = current_distance
        best_route = copy.copy(current_route)
    # 加入禁忌表
    tabu_list.append(candidate[best_index])
    tabu_time.append(tabu_limit)
    current_tabu_num += 1


# -------------- 更新禁忌表以及禁忌期限 -------------- #
def update_tabu():
    global current_tabu_num
    global tabu_time
    global tabu_list
    del_num = 0
    temp = [0 for col in range(len(initial_solution[0]))]
    # 更新步长
    tabu_time = [x - 1 for x in tabu_time]
    # 如果达到期限，释放
    # 将禁忌时间为0的解放出
    for i in range(current_tabu_num):
        if tabu_time == 0:
            del_num += 1
            tabu_list[i] = temp
    current_tabu_num -= del_num  # 放出一组解，禁忌数量要减1
    while 0 in tabu_time:
        tabu_time.remove(0)
    while temp in tabu_list:
        tabu_list.remove(temp)


# -------------- 打印结果输出 -------------- #
def solve():
    runtime = int(input("迭代次数："))
    setup()
    for rt in range(runtime):
        get_candidate()
        update_tabu()
    print("初始解以及初始损失时间： ")
    print(initial_solution)
    print(function(initial_solution))
    print('近似最优解以及近似最小总损失时间： ')
    print(best_route)
    print(best_distance)


if __name__ == '__main__':
    # print(distance[0])   # 学校到各个家庭的距离
    # print(shdic)        # 学校和家庭之间的距离字典
    # print(stohome)      # 学校和家庭之间的距离字典
    solve()
