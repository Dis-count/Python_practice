# -*- coding:utf-8 -*-
# 06-29-2020 The first class
# tuple  immutable
def my_min(a,b):
    if a<b:
        return a
    else:
        return b

my_min(1.4,2)

# dictionary key:value  key are immutable
course = {'date science': 28,'linux': 23, 'statistics': 28}
course['linux']
'statistics' in course
course['math'] = 50

# strings
s = '  Hi, everyone! welcome to the best ML! '
[i.strip(',!') for i in s.lower().split()]

# I/O
f = open('myfile.txt','w')
f.write('This is line #1\n')
f.write('This is the second line\n')
f.close()
f = open('myfile.txt','r')
for line in f:
    print(line)
f.close()

# pandas
import pandas as pd
# dataframe(table)/series(column)

#df = pd.read_csv('students.csv')
df = pd.read_csv('students.csv', index_col = 0)

df.head() # THe first five lines

df['hw1']

hw1 = df.hw1

len(hw1)

hw1.index

hw1.values

hw1.values[2:6]

hw1.describe()

hw1.mean()  # min()  max()  sum()  median()

hw1.values.mean()

# position-based selection
hw1.iloc[3]

hw1_sub = hw1.iloc[2:6]

# index-based selection
hw1['Luci']

hw1[4]  # better not to use it.

# Boolean selection
v = [True, False, True, True, False, True, False, True, True, False, False]
hw1[v]

b = (hw1 >= 6)
hw1[b]
