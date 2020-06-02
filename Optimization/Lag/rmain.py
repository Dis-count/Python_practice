import numpy as np
import gurobipy as gp
from gurobipy import GRB
import scipy.sparse as sp

def rmain(A,C,b,x0,lambda0):

    try:

        m = gp.Model("Rmain")

        xx = np.array(A)
        row1 = xx.shape[0]
        col1 = xx.shape[1]

        x = m.addMVar((row1,col1), lb=0, name="e")
        y = m.addMVar((row1,col1), lb=0, name="f")

        # Set objective
        m.setObjective(x.sum()+ y.sum(), GRB.MINIMIZE)
        # Add constraints
        x0 = np.array(x0)

        lambda0 = np.array(lambda0)

        for i in range(row1):

            m.addConstr(x0 @ x[i, :]- x0 @ y[i, :] <= (b[i] - x0 @ xx[i,:]), name="row"+str(i))

        for i in range(row1):

            m.addConstr(x0*lambda0[i] @ x[i,:]- x0*lambda0[i] @ y[i,:] == (lambda0[i]*b[i] - lambda0[i]* x0 @ xx[i,:]) , name="equal"+str(i))

        m.write('Rmain0.lp')

        m.params.outputflag = 0
        m.optimize()

        return m.objVal

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

        m.params.outputflag = 0
        m.optimize()

        return (m.objVal-np.sum(xx))

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')

A = [[-1,1],[6,4],[1,4]]
C = [5,4]
b = [1,24,9]
x0 =[1,2]

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

lambda0,m = sub(A,C,b)

rmain(A,C,b,x0,lambda0)


def bi(self):
#  minimize    |A'-A|
#  subject to  A\lambda == C (bilinear equality)
#              A * x0 <= b
#              \lambda(Ax0-b) == 0  (bilinear equality)
#              x, y, z non-negative (x integral in second version)

    m = gp.Model("opt_adjust")
    A = np.array(self.A)
    mm = A.shape[0]
    n = A.shape[1]
    x1 = m.addVars(mm,n,lb= 0,name="e") # m X n
    x2 = m.addVars(mm,n,lb= 0,name="f") # m X n

    y = m.addVars(mm, lb=0, name="y") # dual m
    m.update()
    m.addConstrs((gp.quicksum(x[i,j]*y[i] for i in range(mm)) == self.C[j]) for j in range(n))

    m.addConstrs((gp.quicksum(x[i,j]*self.x0[j]*y[i] for j in range(n)) == y[i]*self.b[i]) for i in range(mm))

    m.setObjective(gp.quicksum(x[i,j] for i in range(mm) for j in range(n)), GRB.MINIMIZE)
    m.write('bi.lp')
    m.params.outputflag = 0
# First optimize() call will fail - need to set NonConvex to 2
    try:
        m.params.NonConvex = 2
        m.optimize()
        return (m.objVal-np.sum(A))
    except gp.GurobiError:
        print("Optimize failed")
