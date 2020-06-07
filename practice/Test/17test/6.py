# 如果一个数字能表示为p^q(^表示幂运算)且p为一个素数,q为大于1的正整数就称这个数叫做超级素数幂。现在给出一个正整数n,如果n是一个超级素数幂需要找出对应的p,q。

import sys
import math

def isI(q):
    i=2
    while i<int(math.sqrt(q))+1:
        if q%i==0:
                return False
        i+=1
    return True
print('please input a positive number:')
n = sys.stdin.readline()
n = int(n)
flag = True
for i in range(2,60):
    q = math.pow(n,1.0/i)
    if q % 1  ==  0:  # 是整数的话
        if isI(q):
            flag=False
            print(int(q),i)
            break
if flag:
    print('The number is not a power number.')
