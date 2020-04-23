from gurobipy import *
dualArray=[]
try:

    # Create a new model
    m = Model("mip1")

    # Create variables
    x1 = m.addVar( name="y1")
    x2 = m.addVar( name="y2")
    x3 = m.addVar( name="y3")
    x4 = m.addVar( name="y4")
    # Set objective
    m.setObjective(x1 + x2 + x3 +x4, GRB.MINIMIZE)


    m.addConstr(x1 >= 50, "c0")
    m.addConstr(x2 >= 65, "c1")
    m.addConstr(x3+ 4*x4>= 80, "c2")
    m.optimize()
    
    c = m.getConstrs()  
    for v in m.getVars():
        print('%s = %g' % (v.varName, v.x))
    for i in range(m.getAttr(GRB.Attr.NumConstrs)):
      dualArray.append( c[i].getAttr(GRB.Attr.Pi))#GRB.Attr.SlackGRB.Attr.Pi

    print('Obj: %g' % m.objVal)
    print 'pi:',dualArray
except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
