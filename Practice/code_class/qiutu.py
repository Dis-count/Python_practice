# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:32:29 2017

@author: Discount
"""

def nice(last_turn):
    return 'silence'

def rat(last_turn):
    return 'betray'

def tit_for_tat(last_turn):
    if last_turn == 'betray':
        return 'betray'
    else:
        return 'silence'
    
def prison_delimma(n,s1,s2):
    '''计算不同策略下，经过 n 轮之后犯人各自获刑年限
    n  - 博弈总轮数
    s1 - 犯人一选择的策略
    s2 - 犯人二选择的策略

    '''
    # 初始年数与上轮选择
    p1_years,p2_years = 0
    p1_last_turn,p2_last_turn = ''
    for i in range(n):        # 本轮各自选择
        p1_choice = s1(p2_last_turn)
        p2_choice = s2(p1_last_turn)        # 确定结果
        if p1_choice == p2_choice == 'betray':
            p1_years += 2
            p2_years += 2
        elif p1_choice == p2_choice == 'silence':
            p1_years += 1
            p2_years += 1
        elif p1_choice == 'betray' != p2_choice:
            p2_years += 5
        else:
            p1_years += 5
        # 保存本轮结果
        p1_last_turn,p2_last_turn = p1_choice,p2_choice
    return p1_years,p2_years


