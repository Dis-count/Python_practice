\ Model Rmain
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  e[0] + e[1] + e[2] + e[3] + e[4] + e[5] + f[0] + f[1] + f[2] + f[3] + f[4]
   + f[5]
Subject To
 row0: e[0] + 2 e[1] - f[0] - 2 f[1] <= -0
 row1: e[2] + 2 e[3] - f[2] - 2 f[3] <= 10
 row2: e[4] + 2 e[5] - f[4] - 2 f[5] <= -0
 equal0: = -0
 equal1: 0.8 e[2] + 1.6 e[3] - 0.8 f[2] - 1.6 f[3] = 8
 equal2: 0.2 e[4] + 0.4 e[5] - 0.2 f[4] - 0.4 f[5] = -0
Bounds
End
