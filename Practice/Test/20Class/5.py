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
# Use the StringMethods str

df.Job.unique()

df['Job4'] =  df.Job.str.startswith('Yes') * 0.5 + df.Job.str.contains('full-time') * 0.5

df.Job.str.match('.*part-time.*') * 0.5 + df.Job.str.match('.*full-time.*')*1.0

df.columns

df.drop(columns = ['Job','Job1','Job2','Job3'], inplace = True)

df.rename(columns = {'Job4':'Job'})

# Convert column Bachtime to dummies variables.

dumDF = pd.get_dummies(df, columns = ['BachTime'])

dumDF.columns

cols = dumDF.columns.tolist()

cols[-4:] = ['Batch_0to1','Batch_1to3','Batch_3to5','Batch_5Plus']

dumDF.columns = cols

# change yes to 1 and No to 0
df = dumDF

df.replace({'No': 0, 'Yes': 1}, inplace= True)

# Adding simple columns
df['Language'] = df.C + df.CPP + df.CS + df.Java + df.Python +df.JS + df.R + df.SQL + df.SAS

cols = df.columns.tolist()

cols.insert(0,cols.pop(-1))

df = df.reindex(columns = cols)

# Adding complex columns
# Date \to academic quarter and year

df.Timestamp.astype(np.datetime64).dt.year

####################################
df['Expert'] = (df.Language >= 3)* 1.0

def expertFunction(row):
    if row['Language'] >= 3:
        return 1
    else:
        return 0

df.apply(expertFunction, axis = 1)

df.apply(lambda r: 1 if r['Language'] >= 3 else 0, axis=1)

%timeit df.Language >=3
%timeit df.apply(lambda r: 1 if r['Language'] >= 3 else 0, axis=1)
%timeit df.apply(lambda r: r['Program'].lower(), axis=1)

# solution2 series apply(fast because it uses vectorization)
%timeit df.Program.apply(lambda v: v.lower())

# solution3
%timeit df.Program.str.lower()

# write it to a file

df.to_csv('cleaned_survey.csv')

# Problems
# how many students know SQL?
df.SQL.sum()

df[df.Program == 'MSIS'].ProgSkills.mean()
df[df.Program == 'MBA']['ProgSkills'].mean()

(df.Classification > df.Clustering).sum()
(df.Classification < df.Clustering).sum()

# Some analysis
# Summary statistics
df.Classification.describe()

df.corr()

# find the strongest correlations

cor = df.corr()
cor.stack()

cor[cor < 1].stack().nlargest(20).iloc[::2]

cor.stack().nsmallest(20).iloc[::2]

cor.stack().abs().nsmallest(20)
