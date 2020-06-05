# 牛牛的好朋友羊羊在纸上写了n+1个整数，羊羊接着抹除掉了一个整数，给牛牛猜他抹除掉的数字是什么。牛牛知道羊羊写的整数重新排序之后是一串连续的正整数，牛牛现在要猜出所有可能是抹除掉的整数。例如：
# 10 7 12 8 11 那么抹除掉的整数只可能是9
# 5 6 7 8 那么抹除掉的整数可能是4也可能是9
# 思路：对串排序。然后用最大值减最小值，如果差为n，则涂抹的是中间数字；如果差为n-1，则涂抹两边数字；其他，mistake。先判断是否有重复数字。注意最小值为1的情况。

def get_the_lose_one(data):
    data_ordered = sorted(data,key = lambda x,y:x-y)

    outcome= []
    for index,data in enumerate(data_ordered):
        if index == len(data_ordered)-2:
            break
            if data+1 != data_ordered[index+1]:
            outcome.append(data+1)
            if len(outcome) >= 1:
                print('mistake')
            elif not len(outcome):
                print([data_ordered[0]-1,data_ordered[len(data_ordered)-1]+1])
            else:
                print(outcome[0])
