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

# what is michael's hw1 score
hw1['Michael']
# select the last
hw1.iloc[-1] # just value but without name # is just a element so is a list
hw1.iloc[-1:] # why difference  # [-1:] is range means subset so is a series format.
hw1.iloc[-2:-1]
hw1.iloc[[-1,-3]]

# Compute the average hw1 grade among those students whose grade is less than or equal to 6
hw1[hw1<=6].mean()

# Select those students whose scores is less than 5 or greater than 9
# watch out the priority

hw1[(hw1<5) | (hw1>9)]

# find the max
hw1[hw1 == hw1.max()]

# more series methods
# ranks  if two students are equal, then the rank will be 0.5
hw1.rank()
hw1.rank(ascending=False)

hw1.rank(ascending=False, method = 'min')
hw1.rank(ascending=False, method = 'dense')

# idmax  and  idmin
hw1.idxmax()
hw1.idxmin()

# sort values
hw1.sort_values(ascending = False) # ascending by default

hw1.sort_index()

# nlargest and nsmallest
hw1.nlargest(3)

# head and tail
hw1.tail(3)

# explore the parameters of the methods
hw1.rank(ascending = False,method ='min')

# Who got the 4th highest grade
hw1.nlargest(4).tail(1)
# if there are two are equal
hw1[hw1.rank(ascending = False,method ='min') == 5]

hw1.nlargest(4).iloc[3:4]

#  retrieve the row of the person who comes last in alphabetical order
hw1.sort_index().tail(1)
hw1.sort_index().iloc[-1:]

# 'J' who got the highest grade

hw1[(hw1.index >= 'J') & (hw1.index < 'K')].idxmax()

import numpy as np

hw1.astype(np.str)

hw1 +2

hw1.astype(np.str) + '2'

hw2 = df['hw2']

hw1 + hw2

(hw1 + hw2)/2  # index consistent

hw1 - hw1.mean() + 8

((hw1 + hw2)/2 - 6.7).abs().idxmin()

((hw1 + hw2)/2 - 6.7).abs().nsmallest(1)
