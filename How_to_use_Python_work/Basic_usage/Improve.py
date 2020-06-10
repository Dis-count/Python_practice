# python一直被病垢运行速度太慢，但是实际上python的执行效率并不慢，慢的是python用的解释器Cpython运行效率太差。

# “一行代码让python的运行速度提高100倍”这绝不是哗众取宠的论调。

# 我们来看一下这个最简单的例子，从1一直累加到1亿。
# 原始代码

import time
def foo(x,y):
        tt = time.time()
        s = 0
        for i in range(x,y):
                s += i
        print('Time used: {} sec'.format(time.time()-tt))
        return s

print(foo(1,100000000))


from numba import jit
import time
@jit
def foo(x,y):
        tt = time.time()
        s = 0
        for i in range(x,y):
                s += i
        print('Time used: {} sec'.format(time.time()-tt))
        return s
print(foo(1,100000000))

# 100亿质数优化
import math
import numba
@numba.jit()
def cur(size):
    sieve = [True] * size
    sieve[0] = False
    sieve[1] = False
    if size == 2:
        return sieve
    factor = [index for index, val in enumerate(cur(int(math.sqrt(size)+1))) if val]
    for i in factor:
        k = i * 2
        while k < size:
            sieve[k] = False
            k += i
    return sieve

def up(size):
    sieve = cur(size)
    return sum(1 for x in sieve if x)

up(1000000)
