# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 23:18:15 2017

@author: Discount
"""

# 罗马数字转整数
def romanToInt(s):

    d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    res, p = 0, 'I'
    # 逆序逐一遍历
    # 使用逆序的好处在于，每次只需对一位罗马数字进行加或减的操作
    # 使用顺序的话，可能为两位
    for c in s[::-1]:
        if d[c] < d[p]:
            res = res - d[c]
        else:
            res = res + d[c]
        p = c

    return res

# 整数转罗马数字
def intToRoman(self, num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

    # 迭代依次处理