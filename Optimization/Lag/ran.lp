\ Model random
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  9 x[0] + 9 x[1]
Subject To
 ran[0]: - 11 x[0] + 3 x[1] <= 27
 ran[1]: 17 x[0] - 4 x[1] <= 24
 ran[2]: - 11 x[0] - 5 x[1] <= 16
 ran[3]: 6 x[0] + 8 x[1] <= 21
Bounds
 x[0] free
 x[1] free
End
