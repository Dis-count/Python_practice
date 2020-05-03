import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('house_price.csv')

# 去除脏数据
keep_index = (df['rooms'] != '多') & (df['halls'] != '多')
df = df[keep_index]

# 转换数据类型
df['rooms'] = df['rooms'].astype('int')
df['halls'] = df['halls'].astype('int')

# 截取rooms、halls、size和price
X = df[['rooms', 'halls', 'size']]
y = df['price']

print "\n======================scikit-learn第三方库的线性回归算法==========================="
#测试集和训练集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# 训练
linreg = LinearRegression()
linreg.fit(X_train, y_train)

#结果
print "theta参数："
print linreg.coef_

# 预测房价
print "输入：1,1,49 实际值：326,预测值：", linreg.predict(np.array([1, 1, 49]).reshape(1,3))
print "输入：2,1,56.45 实际值：315,预测值：", linreg.predict(np.array([2, 1, 56.45]).reshape(1,3))
print "输入：2,1,58.3 实际值：466,预测值：", linreg.predict(np.array([2, 1, 58.3]).reshape(1,3))
print "输入：3,1,92.33 实际值：1061,预测值：", linreg.predict(np.array([3, 1, 92.33]).reshape(1,3))
print "输入：2,1,76.88 实际值：408,预测值：", linreg.predict(np.array([2, 1, 76.88]).reshape(1,3))
