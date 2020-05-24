# https://zhuanlan.zhihu.com/p/52371462?from_voters_page=true

# 3.1 辅助函数

# 列表推导式/列表解析式
# 列表推导式基于迭代器进行构造，效率高，常用于遍历、过滤、重复计算，快速生成满足要求的序列。
# 形式上使用中括号作为定界符

# 1. if 在后 —— 过滤元素
[expression for exp1 in sequence1 if condition1
            for exp2 in sequence2 if condition2
            ...
            for expn in sequencen if conditionn]

# 符合 condition 条件的值会被储存在列表中，不符合的不保存 (类似于 pass 和 filter 函数)

# 2. if 在前 —— 分段映射
[expression1 if condition1 else expression2 for exp1 in sequence1
                                            for exp2 in sequence2
                                            ...
                                            for expn in sequencen]

# 3. 嵌套循环

[f'{cl}班学生{num}' for cl in list('ABCDE') for num in range(1,6)] # for 从左到右循环
>>> ['A班学生1', 'A班学生2', 'A班学生3', 'A班学生4', 'A班学生5', 'B班学生1', 'B班学生2', 'B班学生3', 'B班学生4', 'B班学生5', 'C班学生1', 'C班学生2', 'C班学生3', 'C班学生4', 'C班学生5', 'D班学生1', 'D班学生2', 'D班学生3', 'D班学生4', 'D班学生5', 'E班学生1', 'E班学生2', 'E班学生3', 'E班学生4', 'E班学生5']


# example1:  列出当前文件夹下的所有 Python 源文件

[filename for filename in os.listdir() if filename.endswith(('.py', '.pyw'))]
# for 循环遍历 os.listdir() 中的所有的文件，if 过滤以 .py, .pyw 结尾的文件

# example2:  判断某个数是否为素数

import math

def isprime(integer):
	integreNotPrime = 0 in (integer % i for i in range(2, int(math.sqrt(integer)) + 1))
	print(f'{integer} {"不" * integreNotPrime}是一个素数')


# 在 gurobipy 模块中，quicksum 相当于 sum 函数及求和符号，但效率更高。
for i in I:
    MODEL.addConstr(quicksum(x[i,j] for j in J)<=5)


for c in C:
    MODEL.addConstr(gurobipy.quicksum(x[d,i,j] for d in D for i in range(0, 24) for j in range(i + 1, 25) if i <= c < j) >= R[c])
# 更进一步，可以写为：MODEL.addConstrs(gurobipy.quicksum(x[d,i,j] for d in D for i in range(0, 24) for j in range(i + 1, 25) if i <= c < j) >= R[c] for c in C)
