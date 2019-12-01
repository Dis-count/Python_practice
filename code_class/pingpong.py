# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:41:27 2017

@author: Discount
"""

def pingpong(n,k=7):
    '''传入一个正整数参数 n 和特殊数 k，返回第 n 个乒乓数

    n - 第 n 个  (index)
    k - 给定的特殊数，默认为 7
    '''
    # count 计数，随着循环增加
    # num 为 第 count 个数时的乒乓数
    # status 为增或减状态，在 正负 1 之间切换，默认为 1

    count,num,status = 1,1,1

    # 断言 n,k 为正整数，否则抛出错误
    assert isinstance(n,int) and n > 0 ,'input error'
    assert isinstance(k,int) and k > 0 ,'input error'

    while count < n:
        # 判断切换条件(很漂亮的方法啊)
        if str(k) in str(count) or count % k == 0:   
            status *= -1
        # 累加或累减
        num += status
        count += 1
    return num

a = []
for i in range(50):
    a.append(pingpong(i+1))
print(a)