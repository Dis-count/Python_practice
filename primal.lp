\ Model primal
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  5 x[0] + 4 x[1]
Subject To
 p[0]: - x[0] + x[1] <= 1
 p[1]: 6 x[0] + 9 x[1] <= 24
 p[2]: x[0] + 4 x[1] <= 9
Bounds
End
