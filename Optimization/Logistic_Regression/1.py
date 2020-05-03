import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 加载Iris数据集
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'category']
print df.head()

# 鸢尾花的分布图
print '----------------鸢尾花的分布图-------------------'
plt.scatter(df.iloc[50:100, 2], df.iloc[50:100, 3],color='red', marker='o', label='versicolor') # 中间50个样本的散点图
plt.scatter(df.iloc[100:150, 2], df.iloc[100:150, 3],color='blue', marker='x', label='virginica') # 后50个样本的散点图
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()
