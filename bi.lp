\ Model opt_adjust
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0,0] + x[0,1] + x[1,0] + x[1,1] + x[2,0] + x[2,1]
Subject To
 qc0: [ x[0,0] * y[0] + x[1,0] * y[1] + x[2,0] * y[2] ] = 5
 qc1: [ x[0,1] * y[0] + x[1,1] * y[1] + x[2,1] * y[2] ] = 4
 qc2: - y[0] + [ 3 x[0,0] * y[0] + x[0,1] * y[0] ] = 0
 qc3: - 24 y[1] + [ 3 x[1,0] * y[1] + x[1,1] * y[1] ] = 0
 qc4: - 9 y[2] + [ 3 x[2,0] * y[2] + x[2,1] * y[2] ] = 0
Bounds
 x[0,0] >= -1
 x[0,1] >= 1
 x[1,0] >= 6
 x[1,1] >= 4
 x[2,0] >= 1
 x[2,1] >= 4
End
