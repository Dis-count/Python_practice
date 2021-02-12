# Merge
%autosave 0

import pandas as pd
pd.set_option('precision', 2)  # show only two decimal digits

# load the survey data
df = pd.read_csv('cleaned_survey.csv', index_col =0)
len(df)

df_programs = pd.DataFrame({'Program': \
    ['MSIS', 'MBA', 'Master of Finance', \
     'Supply Chain Mgmt & Analytics', 'Master of Hacking'],\
    'Units_required': [51, 70, 48, 49, 100]})

df_programs

df.Program.unique()
df_programs.Program.unique()

len(df_programs)

len(df[(df.Program == 'Business Man') | (df.Program == 'Faculty!') | (df.Program == 'MS Finance') | (df.Program == 'MSF') | (df.Program == 'MSBA') | (df.Program == 'MSFA')])

# Merge on columns
# Inner merge(default)
df.merge(df_programs)

df_inner = df.merge(df_programs, left_on = 'Program', right_on = 'Program')


df.merge(df_programs, how = 'left')
df.merge(df_programs, how = 'right')

df.merge(df_programs, how = 'outer')

# Merge on Indices
df_programs_i = df_programs.set_index('Program')

df.merge(df_programs_i, left_on = 'Program', right_index = True)

# Problems
# For each programming skills level, find the average number of units to be completed by students with that programming skill level

df_complete = df.merge(df_programs)

df_complete.groupby('ProgSkills')['Units_required'].mean()
# For each existing program(i.e. for each Program in df_programs), find the units required to complete it and the number of students belonging to that program that responded to the survey.

df.merge(df_programs, how = 'right').groupby('Program').agg({'Units_required': 'mean', 'C':'count'}).rename(columns = {'C':'N_students'})

# For each person in df, the number of weekly hours they are working, assuming that: each required unit of coursework is 0.25 hours a week of work

df_left = df.merge(df_programs, how = 'left')
df_left['hrs_coursework'] = df_left['Units_required'] * 0.25
df_left['hrs_job'] = df_left.Job.apply(lambda x: 0 if x==0 else 20 if x == 0.5 else 40)
df_left['hrs_total'] = df_left['hrs_coursework'] + df_left['hrs_job']

df_left

# How to deal with Nan properly ...
df_left.fillna(0, inplace = True)
df_left.isna().any()

# Data Visualization with Seaborn
import seaborn as sns
import pandas as pd
import numpy as np
%pylab inline

%autosave 0

# adult census income
# predict whether income exceeds 50k/yr based on census data
df = pd.read_csv('adult.csv')
len(df)
df.columns

df.info()
df.shape

# in order to better illustate some of the plots, let's sample only 500 observations.But you shouldn't do it in the project.

df = df.sample(500,random_state = 1)
len(df)
df.corr()


# type of variables

df2 = df.copy()
df2['discretized_age_EW'] = pd.cut(df2.age, 5)

df2['discretized_age_EW'].unique()

# example: discretized age into 5 bins of equal frequency
df2['discretized_age_EF'] = pd.qcut(df2.age,5)

df2['discretized_age_EF'].unique()

# one numeric variable
# age
sns.countplot(df.age)

sns.countplot(y = 'age', data = df)

sns.distplot(df.age)

sns.distplot(df.age, bins = 20)

# education
sns.countplot(x = 'education', data = df)

sns.countplot(y = 'education', data = df)

# race
sns.countplot(x = 'race', data = df)

# discretized_age_EW/EF
sns.countplot(x = 'discretized_age_EW', data = df2)

sns.countplot(x = 'discretized_age_EF', data = df2)

df2.groupby('discretized_age_EF').size()

# One categorical vs one numberic variable
# For each value of 'marital.status', display the mean average
df['marital.status'].unique()
sns.catplot(y = 'marital.status', data = df, x= 'age', aspect = 2)

sns.catplot(y = 'marital.status', data = df, x= 'age', aspect = 2, kind = 'swarm')

sns.catplot(y = 'marital.status', data = df, x= 'age', aspect = 2, kind = 'point')

sns.catplot(y = 'marital.status', data = df, x= 'age', aspect = 2, kind = 'bar')

sns.catplot(y = 'marital.status', data = df, x= 'age', aspect = 2, kind = 'box')

sns.catplot(y = 'marital.status', data = df, x= 'age', aspect = 2, kind = 'violin')

# Two numberic variables(Regression)
df.corr()

sns.regplot(x = 'education.num', y = 'hours.per.week', data = df)

# Two categorical variables vs one numberic variable
# show the mean age by sex and marital status
sns.catplot(x= 'marital.status', y= 'age', hue = 'sex', data = df, kind = 'bar', aspect =3)

sns.catplot(y= 'marital.status', x= 'age', hue = 'sex', data = df, kind = 'box', aspect =3)

# Two numeric(age, education.num) and one categorical variables(sex)
sns.catplot(x = 'education.num', y ='age', hue = 'sex', data = df, kind = 'bar', aspect =3)

# Two categorical(better if ordinal) variables and one numeric variable
# find average capital gain for age and education.numpy
gr = df2.groupby(['education.num', 'discretized_age_EF'])['capital.gain'].mean()
gr

sns.heatmap(gr.unstack(), annot = True)

# four variables: two numeric and two categorical
sns.catplot(x = 'education.num', y ='age', hue = 'sex', col = 'income', data = df, kind = 'bar', aspect =3)

# four variables: one numeric and three categorical
sns.catplot(x = 'marital.status', y ='age', hue = 'sex', col = 'income', data = df, kind = 'box', aspect =3)

# n numeric variables(Pairplots)
sns.pairplot(df[['age','education.num','capital.gain']])
