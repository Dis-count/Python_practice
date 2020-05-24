# 具体问题是Applied Energy期刊文章《Combined heating and cooling networks with waste heat recovery based on energy hub concept 》中的能源枢纽问题（该问题是多目标问题，这里主要是复现这篇文章）

from gurobipy import *
import random
import numpy as np

try:
    # 天然气锅炉的转换率（天然气->热负荷）
    eta_fh_b = 0.85
    # 热泵的转换率（电->热负荷；(eta_eh_hp-1)为电->冷负荷）
    eta_eh_hp = 6
    # 制冷机组的转换率(电->冷负荷)
    eta_eh_ch = 4
    # 电锅炉的转换率(电->热负荷)
    eta_eh_eh = 0.95
    # 热泵的价格（热泵的容量，每1kw需要的钱）
    phi_hp = 230
    # 电的价格（每一度(1kwh)需要的钱）
    phi_e = 0.0327
    # 天然气的价格（每m³的天然气价格，产生一度电的天然气的价格）
    phi_f = 0.016123
    # 电排放二氧化碳的比例（每度电排放的二氧化碳量）
    lambda_e = 0.02072
    # 天然气排放二氧化碳的比例（产生一度电的天然气排放的二氧化碳量）
    lambda_f = 0.17644
    # 热负荷函数的振幅
    A_h = 50000
    # 冷负荷函数的振幅
    A_c = 50000
    # 同时刻 # 5000（Lc >> Lh）  800(Lh >> Lc)
    # t = 1  # 默认第一个时刻
    # 一年的总时刻
    tau = 8760
    # 热负荷函数
    # Lh = A_h + A_h * np.sin(2 * np.pi * t / tau + np.pi / 2)  # 默认负荷
    # 冷负荷函数
    # Lc = A_c + A_c * np.sin(2 * np.pi * t / tau - np.pi / 2)  # 默认负荷
    # print(Lh, Lc)
    # tt = np.sin(2*np.pi*t/tau - np.pi/2)
    # 用户标准电负荷
    Le = 10000
    # 电热的最大容量
    q_eh_max = 5133

    run_cost = ((1 + 0.05) ** 10 - 1) / (0.05 * (1 + 0.05) ** 10)
    # N = 2
    random.seed(1)  # 设置随机种子

    # 产生随机 Tmatrix 和 Cmatrix
    # phi_e = {(i+1, j+1): 0.0327 for i in range(N) for j in range(4) if j == 0}
    # phi_f = {(i+1+N, j+1+N): 0.02072 for i in range(N) for j in range(N)}
    # 第一个目标成本目标的系数矩阵
    Coeff_obj1 = {}
    Coeff_obj2 = {}
    Lh = []
    Lc = []
    for t in range(tau):
        for j in range(4):
            # pe_eh
            if j == 0:
                Coeff_obj1[(t, j)] = phi_e * run_cost
                Coeff_obj2[(t, j)] = lambda_e
            # pe_hp
            if j == 1:
                Coeff_obj1[(t, j)] = phi_e * run_cost
                Coeff_obj2[(t, j)] = lambda_e
            # pe_ch
            if j == 2:
                Coeff_obj1[(t, j)] = phi_e * run_cost
                Coeff_obj2[(t, j)] = lambda_e
            # pf
            if j == 3:
                Coeff_obj1[(t, j)] = phi_f * run_cost
                Coeff_obj2[(t, j)] = lambda_f
        # Lc self.Lc = Individual.A_c + Individual.A_c * np.sin(2 * np.pi * self.t / Individual.tau - np.pi / 2)
        lc = A_c + A_c * np.sin(2 * np.pi * t / tau - np.pi / 2)
        Lc.append(lc)
        lh = A_h + A_h * np.sin(2 * np.pi * t / tau + np.pi / 2)
        Lh.append(lh)

    print(Coeff_obj1)
    # 定义 model
    m = Model('hub')

    # 添加变量       Tmatrix.keys()个变量， 默认系数是0
    x = m.addVars(Coeff_obj1.keys(), vtype=GRB.CONTINUOUS, name='x')
    qhp_size = m.addVar(obj=phi_hp, vtype=GRB.CONTINUOUS, name='qhp_size')
    # print(x)
    # 添加约束
    # 热负荷等式约束
    m.addConstrs((x[t, 3] * eta_fh_b + x[t, 0] * eta_eh_eh + x[t, 1] * eta_eh_hp == Lh[t] for t in range(tau)), 'C1')
    # 冷负荷等式约束
    m.addConstrs((x[t, 2] * eta_eh_ch + x[t, 1] * (eta_eh_hp-1) == Lc[t] for t in range(tau)), 'C2')
    # 有热泵的约束
    m.addConstrs((eta_eh_eh * x[t, 0] <= q_eh_max for t in range(tau)), 'C3')
    # 电锅炉的约束
    m.addConstrs(((eta_eh_hp - 1) * x[t, 1] <= qhp_size for t in range(tau)), 'C4')

    # # 设置多目标 权重 聚合方式
    # m.setObjectiveN(x.prod(Coeff_obj1) + qhp_size * phi_hp + run_cost * phi_e * Le,  index=0, weight=0.5, name='obj1')
    # m.setObjectiveN(x.prod(Coeff_obj2) + lambda_e * Le, index=1, weight=0.5, name='obj2')

    # 设置多目标 优先级 在满足第一个目标最优的前提下，第二个目标最优
    m.setObjectiveN(x.prod(Coeff_obj1) + qhp_size * phi_hp + run_cost * phi_e * Le,  index=0,  priority=1, abstol=0, reltol=0, name='obj1')
    m.setObjectiveN(x.prod(Coeff_obj2) + lambda_e * Le, index=1,  priority=2, abstol=100, reltol=0, name='obj2')

    # 设置logFile的名称
    m.setParam(GRB.Param.LogFile, 'MultiAssignmentLog.log')

    # print('writing......')
    # m.write('hub.lp')

    # 启动求解
    m.optimize()
    # print(x)
    # 获得求解结果

    for t in range(tau):
        print('pe_eh:', x[t, 0])
        print('pe_hp:', x[t, 1])
        print('pe_ch:', x[t, 2])
        print('p_f:', x[t, 3])
        print('Lh:', Lh[t])
        print('Lc:', Lc[t])
    print('qhp_size:', qhp_size)
    for i in range(2):
        m.setParam(GRB.Param.ObjNumber, i)
        print('Obj%d = ' % (i+1), m.ObjNVal)

    # print('writing......')
    # m.write('hub.lp')

except GurobiError:
    print('Error reported')    
