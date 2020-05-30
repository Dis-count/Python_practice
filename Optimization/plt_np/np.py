import numpy as np

nx = np.array([[1,2,3],[4,5,6],[7,8,9]])
m = np.array([8,8,8])
a = np.row_stack((nx,[8,8,8]))        # nx=np.row_stack((nx,m))  给矩阵加一行

a = np.column_stack((a,[8,8,8,8]))    #给矩阵加一列

print(type(a))
print(a)
