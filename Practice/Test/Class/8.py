# supervised learning -- label
# regression  and  Classification
# discrete and continuous
##  Clustering
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
