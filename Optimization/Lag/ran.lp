\ Model random
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  7 x[0] + 2 x[1]
Subject To
 ran[0]: - 7 x[0] + 19 x[1] <= 5
 ran[1]: 7 x[0] - 3 x[1] <= 13
 ran[2]: - 16 x[0] - 20 x[1] <= 22
 ran[3]: 17 x[0] + 5 x[1] <= 18
Bounds
 x[0] free
 x[1] free
End
