from sklearn.model_selection import cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

X, y = load_digits(return_X_y = True)

pipe = make_pipeline(MinMaxScaler(), LogisticRegression(random_state = 42, max_iter = 1000))

scores = cross_validate(pipe, X, y, cv =3, return_train_score = True)

import pandas as pd

df_scores = pd.DataFrame(scores)

df_scores

df_scores.mean()

df_scores[['train_score','test_score']].boxplot()

scores = cross_validate(pipe, X, y, cv =10, return_train_score = True)

df_scores = pd.DataFrame(scores)

df_scores

df_scores[['train_score','test_score']].boxplot()

# Exercise

from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler


X_b, y_b = load_breast_cancer(return_X_y = True)

pipe = make_pipeline(StandardScaler(), SGDClassifier(max_iter = 1000))

scores = cross_validate(pipe, X_b, y_b, cv =10, scoring = 'balanced_accuracy', return_train_score = True)

df_scores = pd.DataFrame(scores)
df_scores

df_scores[['train_score', 'test_score']].boxplot()

pipe.get_params()

from sklearn.model_selection import GridSearchCV

pipe = make_pipeline(MinMaxScaler(), LogisticRegression(solver= 'saga', random_state = 42, max_iter = 5000))

#  adjust the parameters
param_grid = {'logisticregression__C': [0.1, 1.0, 10], 'logisticregression__penalty': ['l2','l1']}

grid = GridSearchCV(pipe, param_grid = param_grid, cv = 3, n_jobs = -1, return_train_score = True)

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 42)

grid.fit(X_train, y_train)

df_grid = pd.DataFrame(grid.cv_results_)

df_grid

import numpy as np
scores = np.array(df_grid.mean_test_score).reshape(3,2)

import mglearn

mglearn.tools.heatmap(scores, xlabel = 'Penalty', xticklabels = param_grid['logisticregression__penalty'], ylabel ='C', yticklabels = param_grid['logisticregression__C'], cmap = 'viridis')

grid.best_params_
grid.best_estimator_

accuracy = grid.score(X_test, y_test)
accuracy

scores = cross_validate(grid, X, y, cv = 3, n_jobs = -1, return_train_score = True)
df_scores = pd.DataFrame(scores)
df_scores

df_scores.mean()


pipe = make_pipeline(StandardScaler(), SGDClassifier(max_iter = 1000))

#  adjust the parameters
param_grid = {'sgdclassifier__loss': ['hinge', 'log'], 'sgdclassifier__penalty': ['l2','l1']}

grid = GridSearchCV(pipe, param_grid = param_grid, cv = 3, n_jobs = -1, return_train_score = True)

scores = cross_validate(grid, X_b, y_b, cv=3, scoring = 'balanced_accuracy', return_train_score = True)

df_scores = pd.DataFrame(scores)

df_scores[['train_score','test_score']].boxplot()

from sklearn.model_selection import train_test_split

X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(X_b, y_b, stratify = y_b, random_state =0, test_size=0.3)

grid.fit(X_train_b, y_train_b)

grid.best_params_
grid.best_estimator_

# see 9.png   summary

from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge


boston = load_boston()
X_train2, X_test2, y_train2, y_test2 = train_test_split(boston.data, boston.target, random_state =0)

pipe = make_pipeline(PolynomialFeatures(), StandardScaler(), Ridge())

param_grid = {'polynomialfeatures__degree':[1, 2, 3], 'ridge__alpha': [0.001,0.01,0.1,1,10,100]}

grid = GridSearchCV(pipe, param_grid = param_grid, cv =5, n_jobs = -1)

grid.fit(X_train2, y_train2)

grid.cv_results_['mean_test_score']

grid.best_params_

grid.score(X_test2, y_test2)


from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

pipe = Pipeline([('preprocessing', StandardScaler()), ('classifier', SVC())])

param_grid = [{'classifier':  [SVC()], 'preprocessing': [StandardScaler],'classifier__gamma': [0.001,0.01,0.1,1,10,100], 'classifier__C': [0.001,0.01,0.1,1,10,100]}, {'classifier': [RandomForestClassifier(n_estimators = 100)], 'preprocessing': [None], 'classifier__max_features': [1, 2, 3]}]

grid = GridSearchCV(pipe, param_grid, cv = 5)

# bug here
grid.fit(X_train_b, y_train_b)

grid.best_params_

grid.best_score_

grid.score(X_test_b, y_test_b)
