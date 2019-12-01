# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:49:39 2017

@author: Discount
"""

g = [3,6,9]
t = [2,5,8]
def race(g,t):
    # 重新分配
    return [(g[0],t[2]),(g[1],t[0]),(g[2],t[1])]

#  附加题
import itertools
tianji = [1,3,5,7,9]
qiwang = [2,4,6,8,10]

def fj2(qiwang,tianji):
    # 获取田忌所有派遣马匹的方式
    tianji_l = list(itertools.permutations(tianji,len(tianji)))    
    # 全部赛果
    res_all_turns = []    
    # 遍历所有的方式
    for i in tianji_l:        
    # 某一轮的比赛结果
        res_one_turn = []        
        # 某一轮比拼中，双方马匹对阵情况
        for horses in zip(i,qiwang):            
            if horses[0] < horses[1]:
                res_one_turn.append('lose')            
            else:
                res_one_turn.append('win')       
        if res_one_turn.count('win') >= 3:
            res_all_turns.append('win')   
    return len(res_all_turns)

print(fj2(qiwang,tianji))