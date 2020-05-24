# The problem could be divided into main problem and restriced main problem
# and subproblem. But notice that the method addconstraints and try except
# print the error for the convinience of finding the error.
# For the help you can try these methods:help and dir # help(math)  dir(math)

# Main problem
# Minimize A'ij-Aij

#!/usr/bin/env python3.7

# Copyright 2020, Gurobi Optimization, LLC

# This example uses the Python matrix API to formulate the Matrix
# problem;

import numpy as np
import scipy.sparse as sp
import gurobipy as gp
from gurobipy import GRB

# len(x) number of rows
# x.ndim  x.shape

# min b\mu
# A'\mu > C   C and b are list and A is Matrix
# return list
def sub(A,C,b):

    try:
        m = gp.Model("sub")

        xx = np.array(A)
        row = xx.shape[0]
        col = xx.shape[1]

        x = m.addMVar(shape=row, lb=0, name="x")
        A = xx.T
        A = sp.csr_matrix(A)
        # Set objective

        obj = np.array(b)
        m.setObjective(obj @ x, GRB.MINIMIZE)

        rhs = np.array(C)
        # Add constraints

        m.addConstr(A @ x >= rhs, name="c")
        m.write('sub.lp')
        # Optimize model
        m.optimize()

        print('The sub-object: %g' % m.objVal)

        return x.X,m

    except gp.GurobiError as e:
        print('Sub-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Sub-Encountered an attribute error')

def main(A,C,b,x0,lambda0): #

    try:

        m = gp.Model("main")

        xx = np.array(A)
        row1 = xx.shape[0]
        col1 = xx.shape[1]

        x = m.addMVar((row1,col1), lb=A, name="x")

        # Set objective
        m.setObjective(x.sum(), GRB.MINIMIZE)
    # Add constraints
        x0 = np.array(x0)

        lambda0 = np.array(lambda0)

        for i in range(row1):

            m.addConstr(x0 @ x[i, :] <= b[i], name="row"+str(i))

        # At most one queen per column
        for i in range(col1):

            m.addConstr(lambda0 @ x[:, i] >= C[i], name="col"+str(i))
        # np.dot(lambda0,)

        for i in range(row1):

            m.addConstr(x0*lambda0[i] @ x[i,:] == lambda0[i]*b[i], name="equal"+str(i))

        m.write('main1.lp')

        # Optimize model
        m.optimize()

        print('The min-adjustment: %g' % (m.objVal-np.sum(xx)))

        return x.X

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')

def rmain(A,C,b,x0,lambda0): #

    try:

        m = gp.Model("Rmain")

        xx = np.array(A)
        row1 = xx.shape[0]
        col1 = xx.shape[1]

        x = m.addMVar((row1,col1), lb=A, name="x")

        # Set objective
        m.setObjective(x.sum(), GRB.MINIMIZE)
    # Add constraints
        x0 = np.array(x0)

        lambda0 = np.array(lambda0)

        for i in range(row1):

            m.addConstr(x0 @ x[i, :] <= b[i], name="row"+str(i))

        for i in range(row1):

            m.addConstr(x0*lambda0[i] @ x[i,:] == lambda0[i]*b[i], name="equal"+str(i))

        m.write('Rmain1.lp')

        # Optimize model
        m.optimize()

        print('The min-adjustment: %g' % (m.objVal-np.sum(xx)))

        return x.X

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')

def primal(A,C,b):

    try:
        m = gp.Model("primal")

        xx = np.array(A)
        row = xx.shape[0]
        col = xx.shape[1]

        x = m.addMVar(shape=col, lb=0, name="x")
        A = sp.csr_matrix(A)
        # Set objective

        obj = np.array(C)
        m.setObjective(obj @ x, GRB.MAXIMIZE)

        rhs = np.array(b)
        # Add constraints

        m.addConstr(A @ x <= rhs, name="p")
        m.write('primal.lp')

        # Optimize model
        m.optimize()

        print('The primal-object: %g' % m.objVal)

        return x.X

    except gp.GurobiError as e:
        print('Sub-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Sub-Encountered an attribute error')

# this funtion judges if lam1 is the subset lam
def setbool(lam,lam1):
    mybool = (lam > 0.0001) * 1.0
    mybool1 = (lam1 > 0.0001) * 1.0

    # find the index
    obj = np.nonzero(mybool)[0]
    obj1= np.nonzero(mybool1)[0]

    setbool = set(obj1)
    return setbool.issubset(obj)

A = [[-1,1],[6,4],[1,4]]
# A = [[-1,1],[6,4]]
C = [5,4]
n = len(C)
b = [1,24,9]
# b = [1,24]
x0 =[1,2]
opt_value = np.dot(C,x0)
lam,m = sub(A,C,b)

AA = rmain(A,C,b,x0,lam)
AA = AA.tolist()

lam1,m1 = sub(AA,C,b)

cal_value = np.dot(lam1,b)

d_value = cal_value - opt_value

# dual variable numbers of 0
while d > 0.001:
# 不符合要求再加入这样的约束
    try:
        AA = main(A,C,b,x0,lam1)

        m.remove(m.getConstrs()[-n:])
        x = m.getVars()
        obj = (lam1 > 0.0001) * 1.0
        m.addConstr(obj @ x >= 0.001, name="adiag")
        AA = sp.csr_matrix(AA.T)
        m.addConstr(AA @ x >= np.array(C), name="c")
        m.optimize()
        lam = lam1
        lam1 = x.X

    except gp.GurobiError as e:
        print('Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Encountered an attribute error')
else:

print('The optimal adjustment is: %g' % (np.sum(AA)-np.sum(A)))


# 查找不可行的约束是哪个
