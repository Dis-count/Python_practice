import sys
print('Plase input your name: ')
name = sys.stdin.readline()
print('Hello ', name)


import sys
try:
    while True:
        print('Please input a number:')
        n = int(sys.stdin.readline().strip('\n')) #strip('\n')表示以\n分隔，否则输出是“字符串+\n”的形式
        print('Please input some numbers:')
        sn = sys.stdin.readline().strip()#若是多输入，strip()默认是以空格分隔，返回一个包含多个字符串的list。
        if sn == '':
            break
        sn = list(map(int,sn.split())) #如果要强制转换成int等类型，可以调用map()函数。
        print(n)
        print(sn,'\n')
except:
    pass

# input()方法和stdin()类似，不同的是input()括号内可以直接填写说明文字。
# 可以看一个简单的例子：
while True:
    n = int(input('Please input a number:\n'))
    sn = list(map(int,input('Please input some numbers:\n').split()))
    print(n)
    print(sn,'\n')
