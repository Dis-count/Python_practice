# m is a Model
dvars = m.getVars()
# get the object of the model
obj_coeffs = m.getAttr('Obj', dvars)
# get the RHS of the model
RHS_coeffs = m.RHS
# only get the dictionary of the constr.
constrs = m.getConstrs()

# dict  

var_index = {v: i for i, v in enumerate(dvars)}

constr_index= {c: i for i, c in enumerate(constrs)}

# get the value of the vars.
solution = m.getAttr('X', vars)
