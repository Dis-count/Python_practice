\ Model random
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  3 x[0] + 3 x[1]
Subject To
 ran[0]: - 16 x[0] + 11 x[1] <= 29
 ran[1]: 8 x[0] - 20 x[1] <= 19
 ran[2]: - 12 x[0] - 10 x[1] <= 7
 ran[3]: 11 x[0] + 13 x[1] <= 21
Bounds
End
