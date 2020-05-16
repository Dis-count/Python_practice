# The problem could be divided into main problem and restriced main problem
# and subproblem. But notice that the method addconstraints and try except
# print the error for the convinience of finding the error.
# For the help you can try these methods:help and dir # help(math)  dir(math)

# Main problem
# minimize A'ij-Aij

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
def Sub(A,C,b):

    try:
        m = gp.Model("sub")

        xx = np.array(A)
        row = xx.shape[0]
        col = xx.shape[1]

        x = m.addMVar(shape=col, lb=0, name="x")
        A = xx.T
        A = sp.csr_matrix(A)
        # Set objective

        obj = np.array(b)
        m.setObjective(obj @ x, GRB.MINIMIZE)

        rhs = np.array(C)
        # Add constraints

        m.addConstr(A @ x >= rhs, name="c")

        # Optimize model
        m.optimize()

        print('The sub-object: %g' % m.objVal)

        return x.X

    except gp.GurobiError as e:
        print('Sub-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Sub-Encountered an attribute error')

def Main(A,C,b,x0,lambda0): #

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

        print('The min-adjustment: %g' % m.objVal-np.sum(xx))

        return x.X

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')


A = [[-1,1],[6,4]]

C = [5,4]

b = [1,24]

x0 =[2,2.5]

lam = Sub(A,C,b)
AA = Main(A,C,b,x0,lam)

lam1 = Sub(AA,C,b)

data = [1,2,0,3]
exist = (lam > 0.0001) * 1.0


# dual variable numbers of 0
while
# 不符合要求再加入这样的约束
m.addConstr(obj @ x > 0, name="adiag"+str(i))
