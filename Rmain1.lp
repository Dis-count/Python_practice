\ Model Rmain
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0] + x[1] + x[2] + x[3] + x[4] + x[5]
Subject To
 row0: x[0] + 2 x[1] <= 1
 row1: x[2] + 2 x[3] <= 24
 row2: x[4] + 2 x[5] <= 9
 equal0: = -0
 equal1: 0.8 x[2] + 1.6 x[3] = 19.2
 equal2: 0.2 x[4] + 0.4 x[5] = 1.8
Bounds
 x[0] >= -1
 x[1] >= 1
 x[2] >= 6
 x[3] >= 4
 x[4] >= 1
 x[5] >= 4
End
