import matplotlib.pyplot as plt
import pandas as pd
import gurobipy as grb

# m = grb.read("miplib/instances/miplib2010/aflow40b.mps.gz")
# nzs = pd.DataFrame(get_matrix_coo(m),columns=['row_idx', 'col_idx', 'coeff'])
# plt.scatter(nzs.col_idx, nzs.row_idx, marker='.', lw=0)

def get_expr_coos(expr, var_indices):
    for i in range(expr.size()):
        dvar = expr.getVar(i)
        yield expr.getCoeff(i), var_indices[dvar]

def get_matrix_coos(m):
    dvars = m.getVars()
    constrs = m.getConstrs()
    var_indices = {v: i for i, v in enumerate(dvars)}
    for row_idx, constr in enumerate(constrs):
        for coeff, col_idx in get_expr_coos(m.getRow(constr), var_indices):
            yield row_idx, col_idx, coeff

def get_matrix(m):
    dvars = m.getVars()
    constrs = m.getConstrs()
    var_indices = {v: i for i, v in enumerate(dvars)}
    aa = np.zeros((len(constrs),len(dvars)))
    for row_idx, constr in enumerate(constrs):
        for coeff, col_idx in get_expr_coos(m.getRow(constr), var_indices):
            aa[row_idx,col_idx] = coeff
    return aa


nzs = pd.DataFrame(get_matrix_coos(model),
                    columns=['row_idx', 'col_idx', 'coeff'])

plt.scatter(nzs.col_idx, nzs.row_idx,
        marker='.', lw=0)
