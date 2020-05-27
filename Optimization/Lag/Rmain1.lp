\ Model Rmain
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9]
   + x[10] + x[11] + x[12] + x[13]
Subject To
 row0: 0.6 x[0] + x[1] <= 17
 row1: 0.6 x[2] + x[3] <= 11
 row2: 0.6 x[4] + x[5] <= 21
 row3: 0.6 x[6] + x[7] <= 7
 row4: 0.6 x[8] + x[9] <= 5
 row5: 0.6 x[10] + x[11] <= 25
 row6: 0.6 x[12] + x[13] <= 10
 equal0: = -0
 equal1: 0.1666666666666667 x[2] + 0.2777777777777778 x[3]
   = 3.055555555555556
 equal2: = -0
 equal3: 0.1666666666666667 x[6] + 0.2777777777777778 x[7]
   = 1.944444444444445
 equal4: = -0
 equal5: = -0
 equal6: = -0
Bounds
 x[0] >= 12
 x[1] >= 5
 x[2] >= 15
 x[3] >= 2
 x[4] >= 3
 x[5] >= 17
 x[6] >= -15
 x[7] >= 16
 x[8] >= 7
 x[9] >= -17
 x[10] >= -11
 x[11] >= -8
 x[12] >= 13
 x[13] >= 2
End
