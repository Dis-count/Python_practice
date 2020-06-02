\ Model sub
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  18 x[0] + 12 x[1] + 19 x[2] + 15 x[3] + 25 x[4] + 6 x[5]
Subject To
 c[0]: x[0] + 14 x[1] - 7 x[2] + 15 x[3] - 5 x[4] + 4 x[5] = 9
 c[1]: 16 x[0] + 11 x[1] + 7 x[2] - 5 x[3] - 14 x[4] + 2 x[5] = 1
Bounds
End
