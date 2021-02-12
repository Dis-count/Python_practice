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


# Advanced : retrieve unaggregated rows (apply)
df[df.Languages == df.Languages.max()]

df.groupby('Program').apply(lambda d: d[d.Languages == d.Languages.max()])

# Notice that apply is a slow way
%timeit df.groupby('Program')['ProgSkills'].mean()

%timeit df.groupby('Program').apply(lambda d: d.ProgSkills.mean())

# find the students with the highest Classification skills and show their C/Java
# M1
df.loc[df.Classification == df.Classification.max(), ['C','Java']]

df[df.Classification == df.Classification.max()]

# M2
df.groupby('ProgSkills').apply(lambda d: d.loc[d.Classification ==  d.Classification.max(), ['C','Java']])

# For each ProgSkills level, find the Program with most students that have that ProgSkills level
df.groupby('Program').size().nlargest(1)

df.groupby('ProgSkills').apply(lambda d: d.groupby('Program').size().nlargest(1))

# For each ProgSkills level, find the student with the highest Classification skills and show their knowledge of C/java

df.groupby('ProgSkills')['Classification'].agg('max')

df2 = df.copy()

df2['max_classif_within_progskills'] = \
df2.groupby('ProgSkills')['Classification'].transform('max')

df2[df2.Classification == df2.max_classif_within_progskills]

# Create a 0-1 column whose value is 1 if the student knows more languages than the average student of his/her program.
df.groupby('Program')['Languages'].mean()

df2 = df.copy()
df2['avg_languages'] = \
df2.groupby('Program')['Languages'].transform('mean')

df2.Languages > df2.avg_languages

(df2.Languages > df2.avg_languages) * 1

# Make a 0-1 column that indicates whether a student knows clustering better than the average student in his/her quarter(quarter,year).

df2 = df.copy()

df2['baseline_clustering'] = \
df2.groupby(['quarter','year'])['Clustering'].transform('mean')

(df2.Clustering > df2.baseline_clustering) * 1
