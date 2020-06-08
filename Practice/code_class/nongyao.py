# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:38:44 2017

@author: Discount
"""

import itertools
# 装满 6 格，金额小于 10000
equipment = [690,1500,2100,1740,2140,2080]
def func():
    iter = itertools.combinations_with_replacement(equipment,6)
    count = 0
    for i in iter:        
        if sum(i) < 10000:
            print(i)
            count += 1
    return count
print(func())

