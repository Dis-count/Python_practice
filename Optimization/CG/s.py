from gurobipy import *
dualArray=[]
try:

    # Create a new model
    m = Model("sip1")

    # Create variables
    x1 = m.addVar( name="m1")
    x2 = m.addVar( name="m2")
    x3 = m.addVar( name="m3")

    # Set objective
    m.setObjective(x1 + x2 + 0.25*x3 , GRB.MAXIMIZE)


    m.addConstr(56*x1+78*x2 +30*x3<= 120, "c0")
  # m.addConstr(x2 >= 65, "c1")
    #m.addConstr(x3 >= 65, "c2")
    m.optimize()
    
    c = m.getConstrs()  
    for v in m.getVars():
        print('%s = %g' % (v.varName, v.x))
 

    print('Obj: %g' % m.objVal)
  
except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
