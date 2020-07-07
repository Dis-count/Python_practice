import pandas as pd
import numpy as np

df = pd.read_csv('data science survey.csv')
df.head()

df.shape

# change long name / Yes,no \to  1/0
df.columns
df.columns = ['Timestamp','Job','BachTime','Program','ProgSkills','C','CPP','CS','Java','Python','JS','R','SQL','SAS','Excel','Tableau','Regression','Classification','Clustering']

df.rename(columns = {'Program':'MasterProgram'})

df.head()

df.Regression
df.Regression.nunique()
df.Regression.value_counts(dropna = False)  # include the missing value.

# Missing values
df.isna() # Return false or true

df.isna().sum()

# return the row with null values
df[df.Program.isna()]

# is there any student with at least two null values

df[df.isna().sum(axis = 1) >=2]

df.loc[75]

# what to do with null values?
# please see screenshot 5.png.  follow the step 123...

# option1
# Set Null values in Yes/no columns to 0
df.columns

df.Java.unique()

yes_no_cols = []

for c in df.columns:
    if 'Yes' in df[c].unique():
        yes_no_cols.append(c)

df[yes_no_cols] = df[yes_no_cols].fillna('No')

# option2
# Remove the rows that have null values.
df.dropna(subset = ['Program'])

df = df[~df.Program.isna()]

df.Classification.mean()

df.Classification.isna()
df.loc[df.Classification.isna(),'Classification'] = df.Classification.mean()

df.loc[df.Classification.isna(),'Clustering'] = df.Clustering.mean()

# option3
# replace job with 0 (no job) 0.5(part-time) 1(full-time)
df.Job.unique()
# create a column 'Job1' through df.loc

df.loc[df['Job'] == "No, I'm not working at the moment", 'Job1'] = 0.5

df.loc[df['Job'] == "Yes, I have a full-time job", 'Job1'] = 1

df["Job1"] = (df['Job'] == 'Yes, I have a part-time job') * 0.5 + (df['Job'] == 'Yes, I have a full-time job')* 1.0

# solution2
# write a function
# you can use it for many times.

def job2number(jd):
    if jd.startswith('No'):
        return 0
    elif 'part-time' in jd:
        return 0.5
    else:   # full-time
        return 1
df['Job2'] = df.Job.apply(job2number)

df

# solution 3
# use lambda function
# Instead of declaring a funtion as above
df.Job.apply(lambda v: 0 if v.startswith('No') else .5 if 'part-time' in v else 1)

df.loc[:,'Job3'] = df.Job.apply(lambda v: 0 if v.startswith('No') else .5 if 'part-time' in v else 1)

# solution 4
