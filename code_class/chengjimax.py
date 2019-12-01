# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 23:01:54 2017

@author: Discount
"""

def product(num):
    # 数字转为字符串
    num2str = str(num)    
    # 预设最大的结果
    max_num = 0
    len_str = len(num2str)    
    for i in range(1,len_str):        
        # 分别得到字符串两边
        left = num2str[:i]
        right = num2str[i:]
        res = int(left) * int(right)        
        # 如果现在的乘积超过目前的乘积，则更新最大值
        if res > max_num:
            max_num = res    
    return max_num

print(product(123456))

# method 2
def product(num):
    # 转为字符串并获取长度
    len_str = len(str(num))    
    # 预设最大值
    max_num = 0
    for i in range(1,len_str):        
        # 分别得到数字两边
        left = num//(10**i)
        right = num%(10**i)
        res = left * right        
        # 判断是否更新
        if res > max_num:
            max_num = res    
    return max_num

print(product(123456))

#  附加题
def product_2(num):
    num2str = str(num)
    max_num = 0
    for n in itertools.permutations(num2str):
        mixnumber = "".join(n)        
        # 调用之前的 product 函数
        res = product(int(mixnumber))        
        if res > max_num:
            max_num = res    
    return max_num