import numpy as np
import scipy.sparse as sp
import gurobipy as gp
from gurobipy import GRB

# 逆优化给约束矩阵 A,C,b
class INV(object):
    def __init__(self, A, b, C, x0):
	    self.A, self.b, self.C, self.x0= A, b, C, x0
	    print('INV MODEL RUNING...')
    # 用于计算原问题
    def primal(self):

        try:
            m = gp.Model("primal")
            xx = np.array(self.A)
            row = xx.shape[0]
            col = xx.shape[1]

            x = m.addMVar(shape=col, lb=0, name="x")
            A = sp.csr_matrix(self.A)
            # Set objective

            obj = np.array(self.C)
            m.setObjective(obj @ x, GRB.MAXIMIZE)

            rhs = np.array(self.b)
            # Add constraints

            m.addConstr(A @ x <= rhs, name="p")
            m.write('primal.lp')
            m.params.outputflag = 0
            # Optimize model
            m.optimize()

            print('The primal-object: %g' % m.objVal)
            self.result = x.X
            return self.result

        except gp.GurobiError as e:
                print('Primal-Error code ' + str(e.errno) + ": " + str(e))

        except AttributeError:
            print('Primal-Encountered an attribute error')

    def main(A,C,b,x0,lambda0): #

        try:

            m = gp.Model("main")

            xx = np.array(self.A)
            row1 = xx.shape[0]
            col1 = xx.shape[1]

            x = m.addMVar((row1,col1), lb=self.A, name="x")

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

    def adjust(self):

        AA = np.array(self.A)
        CC = np.array(self.C)
        ratio = np.dot(CC,self.x0)/self.b
        adjust = [sum(abs(AA[i,:]*ratio[i]-CC)) for i in range(len(AA[:,0]))]
        min_ad = min(adjust)
        self.ind = adjust.index(min_ad)
        print('The min adjustment is:%g and the index is %g' % (min_ad,self.ind+1))
        return None

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
        x = m.addVars(mm,n,lb= A,name="x") # m X n
        y = m.addVars(mm, lb=0, name="y") # dual m
        m.update()
        m.addConstrs((gp.quicksum(x[i,j]*y[i] for i in range(mm)) == self.C[j]) for j in range(n))

        m.addConstrs((gp.quicksum(x[i,j]*self.x0[j]*y[i] for j in range(n)) == y[i]*self.b[i]) for i in range(mm))

        m.setObjective(gp.quicksum(x[i,j] for i in range(mm) for j in range(n)), GRB.MINIMIZE)
        m.write('bi.lp')
    # First optimize() call will fail - need to set NonConvex to 2
        try:
            m.params.NonConvex = 2
            m.optimize()
        except gp.GurobiError:
            print("Optimize failed")
        return None

# a = np.random.randint(50,size= (4,5))

def rand(m,n):
    A = np.random.randint(20, size= (m,n))
    b = np.random.randint(5,30, size = m)
    C = np.random.randint(10, size = n)
    model = gp.Model('random')
    x = model.addMVar(shape=n, lb=0, name='x')
    AA = sp.csr_matrix(A)
    obj = np.array(C)
    model.setObjective(obj @ x, GRB.MAXIMIZE)
    rhs = b
    model.addConstr(AA @ x <= rhs, name='ran')
    # model.addConstrs(gp.quicksum(A[i,j]* x[j] for j in range(n)) <= rhs[i] for i in range(m))

    model.write('ran.lp')
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
        return model
    else:
        return model

# Con = model.getConstrs()[:]
# print(Con[0].index)

if __name__ == '__main__':
    A = [[-1,1],[6,4],[1,4]]
    C = [5,4]
    b = [1,24,9]
    x0 = [3,1]
    model = rand(3,2)
    A = model.getConstrs()

    xx = INV(A, b, C, x0)
    xx.adjust()
    xx.bi()
    print(xx.primal())
