\ Model random
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  x[0] + 2 x[1]
Subject To
 ran[0]: 4 x[0] + 17 x[1] <= 8
 ran[1]: 2 x[0] + 15 x[1] <= 16
 ran[2]: 12 x[0] + 5 x[1] <= 12
 ran[3]: - 7 x[0] + 7 x[1] <= 26
 ran[4]: 10 x[0] - 10 x[1] <= 5
 ran[5]: - 8 x[0] - 20 x[1] <= 28
 ran[6]: 10 x[0] + 10 x[1] <= 10
Bounds
 x[0] free
 x[1] free
End
