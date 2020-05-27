\ Model sub
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0] + 24 x[1] + 9 x[2]
Subject To
 c[0]: - x[0] + 6 x[1] + x[2] >= 5
 c[1]: x[0] + 4 x[1] + 4 x[2] >= 4
Bounds
End
