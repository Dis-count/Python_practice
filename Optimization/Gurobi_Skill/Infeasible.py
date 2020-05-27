model = Model()
vars = model.getVars()
constrs = model.getConstrs()

for i in range (len(constrs)):
    print (constrs[i].getAttr(GRB.Attr.IISConstr))
for i in range(len(solution)):
    print (solution[i].getAttr(GRB.Attr.IISLB), "  ", vars[i].getAttr(GRB.Attr.IISUB))
