d1 = [{'name':'alice', 'score':38}, {'name':'bob', 'score':18}, {'name':'darl', 'score':28}, {'name':'christ', 'score':28}]
l = sorted(d1, key=lambda x:(-x['score'], x['name']))
print(l)

array = [{"age":20,"name":"a"},{"age":25,"name":"b"},{"age":10,"name":"c"}]
array = sorted(array,key=lambda x:x["age"])
print(array)


example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list = sorted(example_list, key=lambda x: x*-1)
print(result_list)

def sq(x):
    return(x*x)

print(list(map(sq,[y for y in range(10)])))

map(lambda x: x*x,[y for y in range(10)])
# 注意这里map 是生成器 所以要用 list转化才能显示出来，不然只能返回一个地址


c=lambda x,y,z:x*y*z
c(2,3,4)

(lambda x:x**2)(3)

list(filter(lambda x:x%3==0,[1,2,3,4,5,6]))

squares = map(lambda x:x**2,range(5))
print(list(squares))
########

a=[('b',3),('a',2),('d',4),('c',1)]
# 按照第一个元素排序

sorted(a,key=lambda x:x[0])
[('a',2),('b',3),('c',1),('d',4)]
# 按照第二个元素排序

sorted(a,key=lambda x:x[1])
[('c',1),('a',2),('b',3),('d',4)]


from functools import reduce
print(reduce(lambda a,b:'{},{}'.format(a,b),[1,2,3,4,5,6,7,8,9]))
#  （3）嵌套使用将lambda函数嵌套到普通函数中，lambda函数本身做为return的值

def increment(n):
    return lambda x:x+n

f=increment(4)
f(2)


# （4）字符串联合，有默认值，也可以用x=(lambda...)这种格式

x=(lambda x='Boo',y='Too',z='Z00':x+y+z)
print(x('Foo'))

# 在tkinter中定义内联的callback函数

import sys
from tkinter import Button,mainloop

x=Button(text='Press me',command=(lambda :sys.stdout.write('Hello,World\n')))
x.pack()
x.mainloop()


# （6）判断字符串是否以某个字母开头有

Names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
B_Name= filter(lambda x: x.startswith('B'),Names)
print(B_Name)

['Bob', 'Barbara']


# （7）求两个列表元素的和
a = [1,2,3,4]
b = [5,6,7,8]
print(list(map(lambda x,y:x+y, a,b)))

# （8）求字符串每个单词的长度

sentence = "Welcome To Beijing!"
words = sentence.split()
lengths  = map(lambda x:len(x),words)
print(list(lengths))
