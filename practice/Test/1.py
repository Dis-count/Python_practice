# 给出一个正整数N和长度L，找出一段长度大于等于L的连续非负整数，他们的和恰好为N。答案可能有多个，我我们需要找出长度最小的那个。
# 例如 N = 18 L = 2：
# 5 + 6 + 7 = 18
# 3 + 4 + 5 + 6 = 18
# 都是满足要求的，但是我们输出更短的 5 6 7

if __name__ == '__main__':
    N, L = map(int, input().split(' '))
    ## 设定标签值，如果在接下来的程序中没有找到所需结果，最终输出No
    not_find = True
    ## 根据题意 2<=L<=100, 界定循环次数
    for l in range(L, 101):
        ## 根据公式进行计算
        a_start = (2 * N - (l - 1) * l) / (2 * l)
        ## 如果所得结果为整数，即为我们所要找的起始值
        if int(a_start) == a_start:
            not_find = False
            a_start = int(a_start)
            ## 依次输出，并以空格隔开，注意题意要求，最后一位结尾不需要空格，所以单独输出
            for i in range(l - 1):
                print(a_start + i, end=' ')
            print(a_start + l - 1)
            ## 根据题意只需要找到最短的，l是从小到大，所以最先找到的即为所求，不用再进行循环了
            break
    ## 如果没有找到，输出No
    if not_find:
        print("No")
