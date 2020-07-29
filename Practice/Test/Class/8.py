# supervised learning -- label
# regression  and  Classification
# discrete and continuous
##  Clustering -- unsupervised
### 1. K-means

### 2. Hierarchical agglomerative clutering (HAC)

import seaborn as sns
import pandas as pd
import numpy as np
%pylab inline

import warnings
warnings.filterwarnings('ignore')

# we will find clustering in the affairs data set

df = pd.read_csv('affairs.csv', index_col=0)
df = pd.get_dummies(columns = ['occupation'], data=df)
df.head()

df.shape
#  Use K-Means to find 3 clustering

from sklearn.cluster import KMeans
clu = KMeans(n_clusters = 3, random_state = 0)
clu.fit(df)
clu.labels_

df2 = df.copy()
df2['cluster'] = clu.labels_
df2.groupby('cluster').mean()

(df2.age - df2.min())/(df2.max() - df2.min())

df_norm = df.copy()

df_norm = (df_norm - df_norm.mean())/df_norm.std()

clu.fit(df_norm)

df2 = df_norm.copy()
df2['cluster'] = clu.labels_
df2.groupby('cluster').mean()

df2.groupby('cluster').size()

# Getting summary information on the clusters' characteristics


# Finding the best clustering method
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.cluster import Birch
from sklearn.cluster import AgglomerativeClustering

bestSil = -1
for k in range(2,10):
    clus = [KMeans(n_clusters = k, n_jobs = -1), Birch(n_clusters = k), AgglomerativeClustering(n_clusters = k)]
    for cl in clus:
        res = cl.fit(df)
        sil = metrics.silhouette_score(df, res.labels_)
        print(str(cl)[:10] + ' with k =' + str(k) + ': '+ str(round(sil,4)))
        if (sil > bestSil):
            bestSil = sil
            bestCl = cl

bestCl

clu = KMeans(n_clusters = 2, random_state = 0)
clu.fit(df)
clu.labels_

df2 = df.copy()
df2['cluster'] = clu.labels_
df2.groupby('cluster').mean()

##   over-fitting / under-fitting
#  More data/ Regularization(large variance-overfit) //  Add more features/ More complex model.(large bias-underfit)

## Classification for prediction
# methods for training and testing
#1. Hold-out sample:

#2. Cross-validation:

import sklearn as sk

df = pd.read_csv('affairs.csv', index_col =0)
df

(df.affairs == 0).mean()

(df.affairs > 0) * 1.0

df['Cheater'] = (df.affairs > 0) * 1.0

df = pd.get_dummies(df, columns = ['occupation'])

df

X = df.drop(columns = ['affairs','Cheater'])

y = df.Cheater

# Hold-out sample

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
len(X_train)

# Train on the training set

from sklearn.ensemble import RandomForestClassifier
cl = RandomForestClassifier(random_state = 2)
cl.fit(X_train, y_train)
# predict on the test set
y_pred = cl.predict(X_test)
y_pred
(y_pred - y_test).abs().sum()

len(y_test)

(len(y_test) - (y_pred - y_test).abs().sum())/len(y_test)

# Input to Evaluate the performance

# collect scores   // confusion_matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)

# Accuracy   (TN+TP)/n
import sklearn
sklearn.metrics.accuracy_score(y_test, y_pred)

# Precision  精确  TP/(TP+FP)  判罪中 把 FP 后果严重的考虑在内
sklearn.metrics.precision_score(y_test, y_pred)

# Recall 回收率  TP/(TP+FN)   肿瘤中 把 FN 后果严重的考虑在内
sklearn.metrics.recall_score(y_test, y_pred)

# AUC score
cl.predict_proba(X_test)[:,1]

y_proba = cl.predict_proba(X_test)[:,1]

sklearn.metrics.roc_auc_score(y_test, y_proba)

#  Cross-validation
cl

from sklearn.model_selection import KFold
kf = KFold(n_splits = 10, random_state = 0, shuffle = True)

sklearn.model_selection.cross_val_score(cl, X, y, cv = kf, scoring = 'roc_auc')

sklearn.model_selection.cross_val_score(cl, X, y, cv = kf, scoring = 'roc_auc').mean()

# Which classifier obtains the highest performance?
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

clfs = [DecisionTreeClassifier(), sk.ensemble.RandomForestClassifier(n_jobs = -1), sk.naive_bayes.GaussianNB(), sk.linear_model.LogisticRegression(n_jobs = -1), sk.tree.DecisionTreeClassifier(), sk.ensemble.AdaBoostClassifier(),QuadraticDiscriminantAnalysis(), MLPClassifier(), SVC()]
# Let's find the best one in terms of average AUC

maxAUC = -1
bestCL = ''
for cl in clfs:
    kf = KFold(n_splits = 10, random_state = 0, shuffle = True)
    auc = sklearn.model_selection.cross_val_score(cl, X, y, cv = kf, scoring = 'roc_auc').mean()
    if auc > maxAUC:
        bestCL = cl
        maxAUC = auc
    print(str(cl) + ':' + str(auc))

print('**********************')
print(str(bestCL) + ':' + str(maxAUC))

# Basic use-case: train and test a classifier
# We will use digits dataset  which is a dataset of hand-written digits.
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

X, y = load_digits(return_X_y = True)

X[0]

plt.imshow(X[0].reshape(8,8), cmap = 'gray');
plt.axis('off')
print('The digit is {}'.format(y[0]))

from sklearn.model_selection import train_test_split

# 分层 可能不均匀 // 所以最好的 效果是 按 distribution 分层.
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 42)

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state = 42, max_iter = 5000)
# 1000 is not enough for convergence

clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
accuracy

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_jobs = -1, random_state = 42)

clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
accuracy

# load the breast cancer dataset. Import the functions load_breast_cancer from

from sklearn.datasets import load_breast_cancer

X_b, y_b = load_breast_cancer(return_X_y = True)
X_b
X_b.shape

y_b  # 0 for no // 1 for have

from sklearn.model_selection import train_test_split

X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(X_b, y_b, stratify = y_b, random_state =0, test_size=0.3)

# Train a supervised classifier using the training data using GradientBoostingClassifier

from sklearn.ensemble import GradientBoostingClassifier

clf = GradientBoostingClassifier(random_state = 0)

clf.fit(X_train_b, y_train_b)

# Use the fitted classifier to predict the Classification labels for the testing set.
y_pred = clf.predict(X_test_b)

# Computing the balanced accuracy on the testing set. You need to import balanced_accuracy_score from sklearn.metrics
y_pred

from sklearn.metrics import balanced_accuracy_score

accuracy = balanced_accuracy_score(y_test_b, y_pred)

accuracy

# Standardize your data

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state = 42, max_iter = 5000)

clf.fit(X_train, y_train)

print('{} required {} iterations to be fitted'.format(clf.__class__.__name__, clf.n_iter_[0]))

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

clf.fit(X_train_s, y_train)

accuracy = clf.score(X_test_s, y_test)
accuracy

print('{} required {} iterations to be fitted'.format(clf.__class__.__name__, clf.n_iter_[0]))


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

clf.fit(X_train_s, y_train)

accuracy = clf.score(X_test_s, y_test)
accuracy

print('{} required {} iterations to be fitted'.format(clf.__class__.__name__, clf.n_iter_[0]))

## Keep it simple, stupid: use the pipeline
from sklearn.pipeline import Pipeline

pipe = Pipeline(steps = [('scaler', MinMaxScaler()), ('clf', LogisticRegression(random_state = 42))])

from sklearn.pipeline import make_pipeline

pipe = make_pipeline(MinMaxScaler(), LogisticRegression(random_state = 42, max_iter=1000))

pipe.fit(X_train, y_train)

accuracy = pipe.score(X_test, y_test)
accuracy

pipe.get_params()

# Exercise
from sklearn.linear_model import SGDClassifier
pipe = make_pipeline(StandardScaler(), SGDClassifier(max_iter = 1000))
pipe.fit(X_train_b, y_train_b)
y_pred = pipe.predict(X_test_b)
accuracy = balanced_accuracy_score(y_test_b, y_pred)
accuracy

# interactions and polynomials
from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures

boston = load_boston()
X_train2, X_test2, y_train2, y_test2 = train_test_split(boston.data, boston.target, random_state =0)  # 75/25%

sacler = MinMaxScaler()
X_train2_scaled = scaler.fit_transform(X_train2)
X_test2_scaled = scaler.transform(X_test2)

from sklearn.linear_model import Ridge
ridge = Ridge().fit(X_train2_scaled, y_train2)
ridge.score(X_test2_scaled, y_test2)

poly = PolynomialFeatures(degree = 2).fit(X_train2_scaled)
X_train2_poly = poly.transform(X_train2_scaled)
X_test2_poly = poly.transform(X_test2_scaled)
X_train2_scaled.shape

X_train2_poly.shape   #  13 \to 105

poly.get_feature_names()  # 添加项之后 再做scale

ridge = Ridge().fit(X_train2_poly, y_train2)
ridge.score(X_test2_poly, y_test2)

from sklearn.linear_model import Lasso
