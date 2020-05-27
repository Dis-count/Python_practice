\ Model random
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  5 x[1]
Subject To
 ran[0]: 12 x[0] + 5 x[1] <= 17
 ran[1]: 15 x[0] + 2 x[1] <= 11
 ran[2]: 3 x[0] + 17 x[1] <= 21
 ran[3]: - 15 x[0] + 16 x[1] <= 7
 ran[4]: 7 x[0] - 17 x[1] <= 5
 ran[5]: - 11 x[0] - 8 x[1] <= 25
 ran[6]: 13 x[0] + 2 x[1] <= 10
Bounds
End
