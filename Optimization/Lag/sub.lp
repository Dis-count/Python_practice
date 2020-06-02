\ Model sub
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  25 x[0] + 24 x[1] + 27 x[2] + 22 x[3] + 18 x[4] + 24 x[5] + 18 x[6]
   + 11 x[7]
Subject To
 c[0]: 4 x[0] + x[1] + 4 x[2] + 4 x[3] - 13 x[4] + 15 x[5] - 4 x[6]
   + 4 x[7] = -0
 c[1]: 13 x[0] + x[1] + 10 x[2] + 16 x[3] + 15 x[4] - 3 x[5] - 9 x[6]
   + 9 x[7] = 9
Bounds
End
