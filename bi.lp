\ Model opt_adjust
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  e[0,0] + e[0,1] + e[1,0] + e[1,1] + e[2,0] + e[2,1] + f[0,0] + f[0,1]
   + f[1,0] + f[1,1] + f[2,0] + f[2,1]
Subject To
 qc0: - y[0] + 6 y[1] + y[2] + [ e[0,0] * y[0] + e[1,0] * y[1]
   + e[2,0] * y[2] - f[0,0] * y[0] - f[1,0] * y[1] - f[2,0] * y[2] ] = 5
 qc1: y[0] + 4 y[1] + 4 y[2] + [ e[0,1] * y[0] + e[1,1] * y[1]
   + e[2,1] * y[2] - f[0,1] * y[0] - f[1,1] * y[1] - f[2,1] * y[2] ] = 4
 qc2: 0.1 y[0] + [ 2 e[0,0] * y[0] + 3.1 e[0,1] * y[0] - 2 f[0,0] * y[0]
   - 3.1 f[0,1] * y[0] ] = 0
 qc3: 0.4 y[1] + [ 2 e[1,0] * y[1] + 3.1 e[1,1] * y[1] - 2 f[1,0] * y[1]
   - 3.1 f[1,1] * y[1] ] = 0
 qc4: 5.4 y[2] + [ 2 e[2,0] * y[2] + 3.1 e[2,1] * y[2] - 2 f[2,0] * y[2]
   - 3.1 f[2,1] * y[2] ] = 0
Bounds
End
