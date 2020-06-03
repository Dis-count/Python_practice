# 牛牛正在挑战一款名为01翻转的游戏。游戏初始有A个0,B个1，牛牛的目标就是把所有的值都变为1，每次操作牛牛可以任意选择恰好K个数字，并将这K个数字的值进行翻转(0变为1，1变为0)。牛牛如果使用最少的操作次数完成这个游戏就可以获得奖品，牛牛想知道最少的操作次数是多少？
# 例如:A = 4 B = 0 K = 3
# 0000 -> 1110 -> 1001 -> 0100 -> 1111
# 需要的最少操作次数为4

import sys
def main(A, B, K):
    if A == 0: return 0
    if K == 0: return -1
    if A % K == 0: return A / K
    if A & 1 > K & 1 or K >= A + B: return -1
    ret = A // K + 1
    while 1:
        if (ret * K - A) & 1 == 0 and ret * K <= ret * (A + B) - (A, B)[ret & 1]:
            return ret
        ret += 1

print(main(*map(int, sys.stdin.readline().split())))
