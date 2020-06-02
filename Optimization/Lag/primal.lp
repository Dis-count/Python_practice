\ Model primal
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  9 x[0] + x[1]
Subject To
 p[0]: x[0] + 16 x[1] <= 18
 p[1]: 14 x[0] + 11 x[1] <= 12
 p[2]: - 7 x[0] + 7 x[1] <= 19
 p[3]: 15 x[0] - 5 x[1] <= 15
 p[4]: - 5 x[0] - 14 x[1] <= 25
 p[5]: 4 x[0] + 2 x[1] <= 6
Bounds
 x[0] free
 x[1] free
End
