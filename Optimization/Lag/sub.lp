\ Model sub
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  17 x[0] + 11 x[1] + 21 x[2] + 7 x[3] + 5 x[4] + 25 x[5] + 10 x[6]
Subject To
 c[0]: 12 x[0] + 15 x[1] + 3 x[2] - 15 x[3] + 7 x[4] - 11 x[5] + 13 x[6]
   = -0
 c[1]: 5 x[0] + 2 x[1] + 17 x[2] + 16 x[3] - 17 x[4] - 8 x[5] + 2 x[6] = 5
Bounds
End
