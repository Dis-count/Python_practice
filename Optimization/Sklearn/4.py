# 缩放Scale
from sklearn import preprocessing
import numpy as np
a=np.array([[10,2.7,3.6],
            [-100,5,-2],
            [120,20,40]],dtype=np.float64)
print(a)
print(preprocessing.scale(a))#将值的相差度减小
'''
[[  10\.     2.7    3.6]
 [-100\.     5\.    -2\. ]
 [ 120\.    20\.    40
[[ 0\.         -0.85170713 -0.55138018]
 [-1.22474487 -0.55187146 -0.852133  ]
 [ 1.22474487  1.40357859  1.40351318]]
'''
