# 问题描述：判断一个整数 n 是否为 2 的幂次方
def isPow(n):

    return (n & (n - 1)) == 0;

# 问题描述：编号为 1-N 的 N 个士兵围坐在一起形成一个圆圈，从编号为 1 的士兵开始依次报数（1，2，3…这样依次报），数到 m 的 士兵会被杀死出列，之后的士兵再从 1 开始报数。直到最后剩下一士兵，求这个士兵的编号。
def f(n, m):
    if n == 1:   return n
    return (f(n - 1, m) + m - 1) % n + 1;
# 递归解法：old = (new + m - 1) % n + 1

# 问题描述：给你一个整型数组，数组中有一个数只出现过一次，其他数都出现了两次，求这个只出现了一次的数。

def find(arr):
    tmp = arr[0]
    for i in range(1,len(arr)):
        tmp = tmp ^ arr[i]
    return tmp
arr = 1, 2, 3, 4, 5, 1, 2, 3, 4
find(arr)

# 问题描述：给定一个整数 N，那么 N 的阶乘 N! 末尾有多少个 0？例如： N = 10，则 N！= 3628800，那么 N! 的末尾有两个0。
def f(n):
    if n==0: return 0
    return int(n / 5 + f(n / 5))
