# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:53:34 2017

@author: Discount
"""
import math

def goldbach(num):
    #  断言 num 为偶数 并且大于 2
    assert num % 2 == 0 and num >2 , 'num 应为 偶数'
    for i in range(2,num):
        if isprime(i) and isprime(num-i):
            print('{0} 可由两个素数：{1} 和{2}组成'.format(num,i,num-i))
            break

def isprime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    sqrtnum = int(math.sqrt(num))
    for i  in range(3,sqrtnum+1,2):
        if num % i == 0:
            return False
        return True

goldbach(12345678)
