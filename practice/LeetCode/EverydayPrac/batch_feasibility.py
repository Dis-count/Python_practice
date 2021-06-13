# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:04:34 2021

@author: curry
"""
from data import parts,Bin_length,Bin_width,Mach_num
from gurobipy import *
from gurobipy import Model
from gurobipy import GRB
from gurobipy import quicksum


def RandomLS():
    """
    random local search, randomly swap two rectangles"""
    return None

def checkfeasibility(parts,part):
    """
    invoke packing algorithm to check feasibility"""
    result,check = Packing_OpenSpace(parts,part)
#    check = Packing_Gurobi(parts,part)
    if check == False:
        return False
    return True

def print_time(V,H):
    """
    time = recoat velocity * height + scan velocity * volume"""
    recoat = 0.09
    scan = 0.0001
    printime = 1 + recoat*H + scan*V
    return printime

def batch_attributes(parts,part):
    """
    given parts in a batch, output the maximum height,
    total volume and utilization rate"""
    H = max(parts[i]['height'] for i in part)
    V = sum(parts[i]['volume'] for i in part)
    S = sum(parts[i]['length']*parts[i]['width'] for i in part)
    utilization = S/(Bin_width*Bin_length)
    return H,V,utilization

class Openspace(object):
    def __init__(self,coord,width,length):
        self.coord = coord
        self.width = width
        self.length = length

class Part(object):
    def __init__(self,index,coord):
        # 放置part的左下角坐标
        self.index = index
        self.coord = coord

def Packing_OpenSpace(parts,part):
    """
    sequence based parking, coincidently suitable for the genetic algorithm"""
#    random.shuffle(part) #不可把随机列表赋给另一个list，只能在原list上操作
#    p_save = copy.deepcopy(part)
    OS_initial = Openspace((0,0),Bin_width,Bin_length)
    SpaceList = [OS_initial]
    space1 = Openspace((parts[part[0]]['width'],0),Bin_width-parts[part[0]]['width'],Bin_length)
    space2 = Openspace((0,parts[part[0]]['length']),Bin_width,Bin_length-parts[part[0]]['length'])
    SpaceList.extend([space1,space2])
    SpaceList.remove(OS_initial)
    # 添加第一个零件的摆放信息 并从零件列表中去除
    part_pack = [Part(part[0],(0,0))]
    part.remove(part[0])
    dic_space = {}
    while SpaceList!=[] and part!=[]:
        for space in SpaceList:
            dic_space[space.coord] = space   # assmue given coord maps only one openspace
        # Coord_Order is sorted coords bottom left first.
        Coord_Order = sorted([space.coord for space in SpaceList],key = lambda x: (x[1],x[0]))
        Space_BL = dic_space[Coord_Order[0]]
        r = Bestfit(part,Space_BL,SpaceList)
        if r != None:
            part_pack.extend([Part(r,Space_BL.coord)])
            part.remove(r)
            SpaceList = update(r,Space_BL,SpaceList)
        else:
            # if no part can be placed here, the space will be removed
            SpaceList.remove(Space_BL)
    if part != []:
        return None,False
    else:
        result = [part_pack,SpaceList,part,dic_space]
        return result,True

def Bestfit(part,Space_BL,SpaceList):
    """
    if two parts with same fitness value, select one with minimum residual"""
    dic_fitness = {}
    for r in part:
        dic_fitness[r] = cal_fit(r,Space_BL,SpaceList)
    r = max(dic_fitness,key=dic_fitness.get)
    if dic_fitness[r] != -1:
        return r
    else:
        return None

def update(r,Space_BL,SpaceList):
    """
    given current BL coords of the space and the packed part,
    update the open spaces"""
    # 每一次只在自己的 space 内更新
    SpaceList.remove(Space_BL)
    if Space_BL.width-parts[r]['width'] > 0:
        space1 = Openspace((Space_BL.coord[0]+parts[r]['width'],Space_BL.coord[1]),
                       Space_BL.width-parts[r]['width'],Space_BL.length)
    else:
        space1 = None
    if Space_BL.length-parts[r]['length'] > 0:
        space2 = Openspace((Space_BL.coord[0],Space_BL.coord[1]+parts[r]['length']),
                       Space_BL.width,Space_BL.length-parts[r]['length'])
    else:
        space2 = None
    SpaceList = check_overlap(r,Space_BL,SpaceList)
    if space1 != None:
        SpaceList = check_domination(space1,SpaceList)
    if space2 != None:
        SpaceList = check_domination(space2,SpaceList)
    return SpaceList

def check_overlap(r,Space_BL,SpaceList):
    w = parts[r]['width']
    l = parts[r]['length']
    # 如果顶点若不在open space内 则不会有overlap 不动如山
    for space in SpaceList.copy():
        # 若发生变化，则在该space内进行调整 不要越域
        if space.coord[0] <= Space_BL.coord[0]+w and Space_BL.coord[0]+w <= space.coord[0]+space.width:
            if space.coord[1] <= Space_BL.coord[1] + l and Space_BL.coord[1] + l <= space.coord[1]+space.length:
                SpaceList.remove(space)
                # up to 3 are generated, but certain conditions need to be satisfied
                if space.coord[0] != Space_BL.coord[0]:
                    SpaceList = check_domination(Openspace((space.coord[0],space.coord[1]),
                                           Space_BL.coord[0],space.length),SpaceList)
                if space.width-w-Space_BL.coord[0] > 0:
                    SpaceList = check_domination(Openspace((Space_BL.coord[0]+w,space.coord[1]),
                                    space.width-w-Space_BL.coord[0],space.length),SpaceList)
                if space.length-l-Space_BL.coord[1]+space.coord[1] > 0:
                    SpaceList = check_domination(Openspace((space.coord[0],Space_BL.coord[1]+l),
                                    space.width,space.length-l-Space_BL.coord[1]+space.coord[1]),SpaceList)
    return SpaceList

def check_domination(space,SpaceList):
    """
    compared with existing open spaces one by one, newly generated is added iif
    it's not dominated by any other spaces"""
    for r in SpaceList:
        # 避免俩平行但不重叠的space 只是单纯大小不同 所以 M2.x<M1.x+M1.w
        if r.coord[0] <= space.coord[0] and space.coord[0]+space.width <= r.coord[0]+r.width and space.coord[0] < r.coord[0]+r.width:
            if r.coord[1] <= space.coord[1] and space.coord[1]+space.length <= r.coord[1]+r.length and  space.coord[1]<r.coord[1]+r.length:
                return SpaceList
    SpaceList.extend([space])
    return SpaceList

def cal_fit(r,Space_BL,SpaceList):
    if parts[r]['width'] <= Space_BL.width and parts[r]['length'] <= Space_BL.length:
        fitness = 0
        if parts[r]['width'] == Space_BL.width:
            fitness += 1
        if parts[r]['length'] == Space_BL.length:
            fitness += 1
        if len(SpaceList)>=2:
            neighbor1 = SpaceList[1]
            if parts[r]['length'] == neighbor1.coord[1] - Space_BL.coord[1]:
                fitness += 1
        if len(SpaceList)>=3:
            neighbor2 = SpaceList[2]
            if parts[r]['length'] == neighbor2.coord[1] - Space_BL.coord[1]:
                fitness += 1
        return fitness
    else:
        return -1






def Packing_Gurobi(parts,part):
    """
    optimal packing with gurobi,
    compared with packing heuristic based on open space"""

    m = Model('SchedulePacking')
    m.setParam('OutputFlag', 0)
    #variables
    x = m.addVars(part, lb=0, vtype = GRB.CONTINUOUS, name = "x_coord")
    z = m.addVars(part, lb=0, vtype = GRB.CONTINUOUS, name = "z_coord")

    PL = m.addVars(part, parts, vtype = GRB.BINARY, name = "Left")
    PB = m.addVars(part, parts, vtype = GRB.BINARY, name = "Below")

    #constraints
    m.addConstrs( x[i] + parts[i]['width'] <= Bin_width for i in part )
    m.addConstrs( z[i] + parts[i]['length'] <= Bin_length for i in part )
    #record the top right coordinates

    for i in part:
        for j in part:
            if i != j:
                m.addConstr( x[i] + parts[i]['width'] <= x[j] + Bin_width*(1-PL[i,j]) )

    for i in part:
        for j in part:
            if i != j:
                m.addConstr( z[i] + parts[i]['length'] <= z[j] + Bin_length*(1-PB[i,j]) )

    for i in part:
        for j in part:
            if i != j:
                m.addConstr( PL[j,i] + PL[i,j] + PB[j,i] + PB[i,j] >= 1 )

    obj = 1
    m.setObjective(obj, GRB.MINIMIZE)
    m.Params.MIPGap = 0.1
    m.optimize()
    if m.status == GRB.INFEASIBLE:
        check = False
    else:
        check = True
    return check
