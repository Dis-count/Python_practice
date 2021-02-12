import pandas as pd
import numpy as np

df = pd.read_csv('students.csv')

df = df.set_index('Name')
df.index

df.columns
df.values[3]
df.iloc[3,2]  # 4th row   3rd column
df.iloc[2,:]  # Must know the specific location.
df.iloc[2]
df.iloc[:,1]

df.iloc[:4,-2:]  # the 4th rows and the last two columns

df.iloc[[3,5],:]

df.loc['Jeannine','hw2']
df.loc['Jeannine',:]
df.loc['Jeannine']
df.loc[:,'hw1']

df.hw1   # not work for number beginning.
df['hw1']

df.loc[:,['hw1','hw2']]

df.loc['Luci']
df.loc[['Luci','Garland'],['hw1','program']]

(df.index >= 'J') & (df.index < 'K')

df.loc[(df.index >= 'J') & (df.index < 'K'),:]

df.loc['Shelby','hw1']
df.loc['Shelby',:]  # df.loc['Shelby']

df.loc[df['hw2'] == df['hw2'].max(),:]
df[df['hw2'] == df['hw2'].max()] # or df.hw2.max()

df[df.hw2.rank(ascending = False, method = 'min') == 1]

df[df['hw2'] == df['hw2'].max()].loc[:,['hw1','program']]

df[df['hw2'] == df['hw1']]

df[df['hw2'] == df['hw1']].loc[:,['hw1','hw2']]

df[df.hw2 > 5]

df[df.hw2 > 5].hw1.mean()

# sort_values()
df.sort_values(by = 'hw1', ascending = False)

df.sort_values(by = ['hw1','hw2'], ascending = [False,True])

df.sort_index()
# df.head()  df.tail()

df[df.program == 'MSIS'].sort_values(by = ['hw2'], ascending = False)

df.sort_values(by = 'hw2', ascending = False).head(4)['hw1']

df.mean(axis = 1)  # column
df.hw1.mean()

#  compute the spread(highest - lowest) of each student
abs(df.values[:,0] - df.values[:,1])

(df.hw2 - df.hw1).abs()
# Who has the largest spread?
(df.hw2 - df.hw1).abs().nlargest(1)

# modifying dataframes
# Make a copy of the data frame

# Notice that if you use '=' directly, you just use two names to point the same address. So you should just use '= copy'.

df2 = df.copy()

df2.loc['Oliver'] = [np.nan, 8, 'MSIS']

df2 = df.copy()
df2['hw3'] = 0

# Add calculated columns
df2['final'] = 0.2 * df2.hw1 + 0.8 * df2.hw2
