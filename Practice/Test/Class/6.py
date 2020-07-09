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

df.groupby('Program')['Job']

df.groupby('SQL')
