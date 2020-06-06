import numpy as np
import scipy.sparse as sp
import gurobipy as gp
from gurobipy import GRB
from pandas import DataFrame

# 逆优化给约束矩阵 A,C,b
class INV(object):
    def __init__(self, A, b, C, x0):
	    self.A, self.b, self.C, self.x0= A, b, C, x0
	    # print('INV MODEL RUNING...')

    def adjust(self):

        AA = np.array(self.A)
        CC = np.array(self.C)
        ratio = np.dot(CC,self.x0)/self.b
        adjust = [sum(abs(AA[i,:]*ratio[i]-CC)) for i in range(len(AA[:,0]))]
        min_ad = min(adjust)
        self.ind = adjust.index(min_ad)
        # print('The min adjustment is:%g and the index is %g' % (min_ad,self.ind+1))
        return min_ad

    def bi(self):
#  minimize    |A'-A|
#  subject to  A^T\lambda == C (bilinear equality)
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
        m.addConstrs((gp.quicksum((x1[i,j]-x2[i,j]+A[i,j])*y[i] for i in range(mm)) == self.C[j]) for j in range(n))

        m.addConstrs((gp.quicksum((x1[i,j]-x2[i,j]+A[i,j])*self.x0[j]*y[i] for j in range(n)) == y[i]*self.b[i]) for i in range(mm))

        m.setObjective(gp.quicksum((x1[i,j]+x2[i,j]) for i in range(mm) for j in range(n)), GRB.MINIMIZE)
        m.write('bi.lp')
        m.params.outputflag = 0
    # First optimize() call will fail - need to set NonConvex to 2
        try:
            m.params.NonConvex = 2
            m.optimize()
            return m.objVal
        except gp.GurobiError:
            print("Optimize failed")

def rand(m,n):
    A1 = np.random.randint(-20,-1, size= 4)
    A2 = np.random.randint(1,20, size= 4)
    A = np.zeros((m+4,n))
    A[0:m,:] = np.random.randint(1,20, size= (m,n))
    A[m,:] = [A1[0],A2[0]]
    A[m+1,:] = [A2[1],A1[1]]
    A[m+2,:] = [A1[2],A1[3]]
    A[m+3,:] = [A2[2],A2[3]]
    b = np.random.randint(5,30, size = m+4)
    C = np.random.randint(10, size = n)
    model = gp.Model('random')
    x = model.addMVar(shape=n, lb=-GRB.INFINITY, name='x')
    AA = sp.csr_matrix(A)
    obj = np.array(C)
    model.setObjective(obj @ x, GRB.MAXIMIZE)
    model.addConstr(AA @ x <= b, name='ran')
    # model.addConstrs(gp.quicksum(A[i,j]* x[j] for j in range(n)) <= rhs[i] for i in range(m))

    model.write('ran.lp')
    model.params.outputflag=0
    model.optimize()
    #model.remove(model.getConstrs()[:])

    if model.status == GRB.Status.INFEASIBLE:
        print('Optimization was stopped with status %d' % model.status)
        # do IIS, find infeasible constraints
        model.computeIIS()
        for c in model.getConstrs():
            if c.IISConstr:
                print('%s' % c.constrName)
                model.remove(c)
        model.update()
        return model,x.X
    else:
        return model,x.X

def get_expr_coos(expr, var_indices):
    for i in range(expr.size()):
        dvar = expr.getVar(i)
        yield expr.getCoeff(i), var_indices[dvar]

def get_matrix(m):
    dvars = m.getVars()
    constrs = m.getConstrs()
    var_indices = {v: i for i, v in enumerate(dvars)}
    aa = np.zeros((len(constrs),len(dvars)))
    for row_idx, constr in enumerate(constrs):
        for coeff, col_idx in get_expr_coos(m.getRow(constr), var_indices):
            aa[row_idx,col_idx] = coeff
    return aa
# Con = model.getConstrs()[:]
# print(Con[0].index)
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

        m.addConstr(A @ x == rhs, name="c")
        m.write('sub.lp')
        m.params.outputflag = 0
        m.optimize()

        # print('The sub-object: %g' % m.objVal)

        return x.X

    except gp.GurobiError as e:
        print('Sub-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Sub-Encountered an attribute error')

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

def rmainA(A,C,b,x0,lambda0): #

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

def primal(A,C,b):

    try:
        m = gp.Model("primal")

        xx = np.array(A)
        row = xx.shape[0]
        col = xx.shape[1]

        x = m.addMVar(shape=col, lb=-GRB.INFINITY, name="x")
        A = sp.csr_matrix(A)
        # Set objective

        obj = np.array(C)
        m.setObjective(obj @ x, GRB.MAXIMIZE)

        rhs = np.array(b)
        # Add constraints

        m.addConstr(A @ x <= rhs, name="p")
        m.write('primal.lp')
        m.params.outputflag=0
        # Optimize model
        m.optimize()

        #print('The primal-object: %g' % m.objVal)

        return x.X

    except gp.GurobiError as e:
        print('Sub-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Sub-Encountered an attribute error')

if __name__ == '__main__':

    res = np.zeros((100,4))

    for i in range(100):
        model,x0 = rand(0,2)
        # model.optimize()
        x0 = 0.95*x0
        A = get_matrix(model)
        # print(A)
        b = model.RHS
        C = model.getAttr('Obj', model.getVars())
        lamb = sub(A,C,b)
        x1 = primal(A,C,b)
        # print(x0)
        # print(lamb)
#        res3 = rmain(A,C,b,x0,lamb)  # 用绝对值
#        res4 = rmainA(A,C,b,x0,lamb) # 不用绝对值，直接增大
        xx = INV(A, b, C, x0)
        res1 = xx.adjust()  # 用一刀切
        res2 = xx.bi()      # bilinear 使用增大
#        res[i,:] = [res1,res2,res3,res4]
        if res1 < res2:
            print(A,b,C)
            print(res1)
            print(res2)
        break
#    df = DataFrame(res)
#    df.to_excel('1res095.xlsx')

# 存入一个 100*3的矩阵 ，每一行是一个结果
# 将矩阵转为data frame
# 再将df写入 excel中
# test

A = [[ -7 , 19],
    [  7 , -3],
    [-16, -20],
    [ 17,   5]]
b = [5.0, 13.0, 22.0, 18.0]
C = [7.0, 2.0]
0.3186692506459945
0.8075632315625724

x1 = primal(A,C,b)
print(x1)
x1*C
0.95*x1
(13+0.95*x1[1]*3)/(0.95*x1[0])
(18-0.95*x1[1]*5)/(0.95*x1[0])

lamb = sub(A,C,b)
res3 = rmain(A,C,b,0.95*x1,lamb)
print(res3)


m =Model()
v0 = m.addVar()
v1 = m.addVar()
m.update()
m.addConstr(v0 - v1 <= 4) # Constraint 1
m.addConstr(v0 + v1 <= 4) # Constraint 2
m.addConstr(-0.25*v0 + v1 <= 1) # Constraint 3
m.setObjective(v1, GRB.MAXIMIZE) # Objective: maximize v1
m.params.outputflag = 0
m.optimize()

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,10)
y1 = (7*x+5)/19
y2 = (7*x-13)/3
y3 = (-16*x-22)/20
y4 = (-17*x+18)/5
plt.title('Feasible Region.')
plt.plot(x,y1,color='red',linewidth=1,label='y1',linestyle='--',marker='*')
plt.plot(x,y2,color='blue',linewidth=1,label='y2',linestyle='-.',marker='o')
plt.plot(x,y3,color='green',linewidth=1,label='y3',linestyle='dotted')
plt.plot(x,y4,color='orange',linewidth=1,label='y4')
plt.plot(0.95*x1[0],0.95*x1[1],'ro')
plt.legend()
plt.show()
