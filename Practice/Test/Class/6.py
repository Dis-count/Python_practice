## groupby

import pandas as pd

pd.set_option('precision', 2) # show 2 digital

df = pd.read_csv('cleaned_survey.csv', index_col = 0)

df.mean()

gb = df.groupby('Program')
gb.mean()

df.groupby('Job').mean()

# Aggregate only some columns

df.groupby('Program')['Job'].mean()

df.groupby('Program').size()

df.groupby('Program')['Job','C','R'].mean()

# 72.9% know SQL
df.SQL.mean()

df.groupby('Job').SQL.mean()

# Notice the order of operation
df.groupby('Program').SQL.sum()

df[df.SQL == 1].groupby('Program').size()

df.groupby('Program').SQL.count()  # count No but don't count missing value

df[df.SQL == 1].groupby('Program')['Java'].mean()
# the first just mean one column but the second one mean all columns
df.groupby(by = 'Program')['SQL'].mean()
df.groupby(by = 'Program').mean()['SQL']

df[df.Program == 'MBA'].groupby('Classification').size()

df2 = df.copy()

df2['MBA'] = df2.Program == 'MBA'

df2.groupby('Classification')['MBA'].sum()

# apply multiple function
df.groupby('Job')['SQL'].agg(['mean','size','sum'])

# rename the columns manually
df.groupby('Job')['SQL'].agg(['mean','size']).rename(columns = {'mean': 'SQL_prop', 'size': 'n_students'})

# apply multiple arbitrary functions to multiple columns and give them names

result = df.groupby('Job').agg({'SQL': 'mean', 'Classification': ['max', lambda x: x.max()-x.min()]})

result.columns = ['mean_SQL','max_Class','spread_Class']

result

# group by multiple fields
df.groupby('Program').mean()

# Hierarchical index
df.groupby(['Program','Job'], as_index = False).mean()

# P1
df.groupby('Program')['Languages'].agg(['max','min','mean'])

# P2
df.groupby(['ProgSkills','Program']).agg({'Job': 'size', 'Python': 'mean'}).rename(columns = {'Job': 'nStudents','Python':'PythonProp'})

# P3
df1 = df.copy()
df1['PythonAndC'] = df1['Python'] * df1['C']
df1.groupby('Program').agg({'PythonAndC': 'sum', 'Clustering': lambda x: x.max() -x.min()})
