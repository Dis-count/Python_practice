# 牛牛新买了一本算法书，算法书一共有n页，页码从1到n。牛牛于是想了一个算法题目：在这本算法书页码中0~9每个数字分别出现了多少次？

def pcount(x, n):
    a, b, c, i, m = 1, 0, 0, 1, 0
    while a:
        k = x // i
        a = k // 10
        b = k % 10
        c = x % i
        if n > b:
            m += a * i
        elif n == b:
            m += ((a-bool(n==0)) * i + c + 1)
        else:
            m += (a + bool(n)) * i
        i *=10
    return m

inum = int(input())
onum = str(pcount(inum, 0))
for j in range(1, 10):
    onum += (' ' + str(pcount(inum, j)))
print(onum)
