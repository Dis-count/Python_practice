# -*- coding: UTF-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split

"""
通过判定花萼长度，花萼宽度，花瓣长度，花瓣宽度的尺寸大小来识别鸢尾花的类别
前四列分别为：花萼长度（sepal），花萼宽度，花瓣长度（petal），花瓣宽度
第5列为鸢尾花的类别（包括Setosa，Versicolour，Virginica三类）
"""
from sklearn import datasets
iris = datasets.load_iris()

# 加载Iris数据集作为DataFrame对象
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'category']

df = df.iloc[50:150, :]
df.loc[df['category'] == 'Iris-versicolor', 'category'] = 0
df.loc[df['category'] == 'Iris-virginica', 'category'] = 1

df['category'] = df['category'].astype('int')
# 取其中两个特征，即：花瓣长度，花瓣宽度，即第2列和第3列
X = df[['petal_length', 'petal_width']].values
y = df[['category']].values

# plt.scatter(X[:50, 0], X[:50, 1],color='red', marker='o', label='setosa') # 前50个样本的散点图
# plt.scatter(X[50:100, 0], X[50:100, 1],color='blue', marker='x', label='versicolor') # 中间50个样本的散点图
# plt.scatter(X[100:, 0], X[100:, 1],color='green', marker='+', label='Virginica') # 后50个样本的散点图
# plt.xlabel('petal length')
# plt.ylabel('sepal length')
# plt.legend(loc=2) # 把说明放在左上角，具体请参考官方文档
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#对特征进行标准化处理（特征缩放）
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)

X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=1000.0, random_state=0)
lr.fit(X_train_std, y_train.ravel())
print lr.coef_


print '-----------------测试-----------------'
train_right_counts = 0
for i in range(X_train_std.shape[0]):
    original_val = y_train[i, :]
    predict_val = lr.predict(X_train_std[i, :].reshape(1, -1))
    # print "Original:", original_val, " Predict:", predict_val, ("o" if original_val == predict_val else "x")
    if original_val == predict_val:
        train_right_counts += 1

print "训练集准确率：", ((train_right_counts * 1.0) / X_train_std.shape[0])

test_right_counts = 0
for i in range(X_test_std.shape[0]):
    original_val = y_test[i, :]
    predict_val = lr.predict(X_test_std[i, :].reshape(1, -1))
    # print "Original:", original_val, " Predict:", predict_val, ("o" if original_val == predict_val else "x")
    if original_val == predict_val:
        test_right_counts += 1

print "测试集准确率：", ((test_right_counts * 1.0) / X_test_std.shape[0])


# # 化边界函数
# X_combined_std = np.vstack((X_train_std, X_test_std))
# y_combined = np.hstack((y_train, y_test))
#
# plot_decision_regions(X_combined_std, y_combined, classifier=lr, test_idx=range(105,150))
# plt.xlabel('petal length [standardized]')
# plt.ylabel('petal width [standardized]')
# plt.legend(loc='upper left')
# plt.show()
