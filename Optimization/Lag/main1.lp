\ Model main
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0] + x[1] + x[2] + x[3]
Subject To
 row0: 2 x[0] + 2.5 x[1] <= 1
 row1: 2 x[2] + 2.5 x[3] <= 24
 col0: 0.4 x[0] + 0.9 x[2] >= 5
 col1: 0.4 x[1] + 0.9 x[3] >= 4
 equal0: 0.8 x[0] + x[1] = 0.4
 equal1: 1.8 x[2] + 2.25 x[3] = 21.6
Bounds
 x[0] >= -1
 x[1] >= 1
 x[2] >= 6
 x[3] >= 4
End
