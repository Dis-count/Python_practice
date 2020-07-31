%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

import os
data = pd.read_csv('Titanic_0.csv')
data.head()

data.shape

y = data['Survived']
X = data.drop(columns = 'Survived')

X.isna().sum()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state =3)

X_train.isna().sum()

X_train.Embarked.unique()  # where embark.

X_train[['Sex','Embarked']]

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline

ohe = make_pipeline(SimpleImputer(strategy = 'constant'), OneHotEncoder())

X_encoded = ohe.fit_transform(X_train[['Sex', 'Embarked']])

X_encoded.toarray()

X_encoded

col_cat = ['Sex', 'Embarked']
col_num = ['Age', 'SibSp', 'Parch', 'Fare']

X_train_cat = X_train[col_cat]
X_train_num = X_train[col_num]
X_test_cat = X_test[col_cat]
X_test_num = X_test[col_num]

from sklearn.preprocessing import StandardScaler

scaler_cat = make_pipeline(SimpleImputer(strategy = 'constant'), OneHotEncoder())

X_train_cat_enc  = scaler_cat.fit_transform(X_train_cat)
X_test_cat_enc = scaler_cat.transform(X_test_cat)

scaler_num = make_pipeline(SimpleImputer(strategy = 'mean'), StandardScaler())

X_train_num_scaled = scaler_num.fit_transform(X_train_num)
X_test_num_scaled = scaler_num.transform(X_test_num)

X_train_cat_enc

X_train_num_scaled

from scipy import sparse

X_train_scaled = sparse.hstack((X_train_cat_enc, sparse.csr_matrix(X_train_num_scaled)))

X_test_scaled = sparse.hstack((X_test_cat_enc, sparse.csr_matrix(X_test_num_scaled)))

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

clf.fit(X_train_scaled, y_train)

accuracy = clf.score(X_test_scaled, y_test)
accuracy

from sklearn.compose import make_column_transformer

pipe_cat = make_pipeline(SimpleImputer(strategy = 'constant'), OneHotEncoder(handle_unknown = 'ignore'))
pipe_num = make_pipeline(SimpleImputer(strategy = 'mean'), StandardScaler())

preprocessor = make_column_transformer((pipe_cat, col_cat), (pipe_num, col_num))

pipe = make_pipeline(preprocessor, LogisticRegression())

pipe.fit(X_train, y_train)

accuracy = pipe.score(X_test, y_test)

accuracy

param_grid = {'columntransformer__pipeline-2__simpleimputer__strategy':['mean','median'], 'logisticregression__C':[0.1,1,10]}

from sklearn.model_selection import GridSearchCV


grid = GridSearchCV(pipe, param_grid = param_grid, cv= 5, n_jobs = -1, return_train_score =True)

from sklearn.model_selection import cross_validate

scores = pd.DataFrame(cross_validate(grid, X, y, scoring = 'balanced_accuracy', cv= 5, n_jobs =-1,  return_train_score= True))

scores[['train_score','test_score']].boxplot()

# For 预测.csv   how to preprocessing.
