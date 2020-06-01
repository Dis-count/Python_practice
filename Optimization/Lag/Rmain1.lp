\ Model Rmain
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]
Subject To
 row0: 1.725 x[0] + 1.33125 x[1] <= 27
 row1: 1.725 x[2] + 1.33125 x[3] <= 24
 row2: 1.725 x[4] + 1.33125 x[5] <= 16
 row3: 1.725 x[6] + 1.33125 x[7] <= 21
 equal0: = -0
 equal1: 0.1940625 x[2] + 0.149765625 x[3] = 2.7
 equal2: = -0
 equal3: 2.03765625 x[6] + 1.5725390625 x[7] = 24.80625
Bounds
 x[0] >= -11
 x[1] >= 3
 x[2] >= 17
 x[3] >= -4
 x[4] >= -11
 x[5] >= -5
 x[6] >= 6
 x[7] >= 8
End
