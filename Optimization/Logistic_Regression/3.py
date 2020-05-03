"""
通过判定花萼长度，花萼宽度，花瓣长度，花瓣宽度的尺寸大小来识别鸢尾花的类别
前四列分别为：花萼长度（sepal），花萼宽度，花瓣长度（petal），花瓣宽度
第5列为鸢尾花的类别（包括Setosa，Versicolour，Virginica三类）
"""
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

print '----------------数据预处理-------------------'
df = df.iloc[50:150, :]
df.loc[df['category'] == 'Iris-versicolor', 'category'] = 0
df.loc[df['category'] == 'Iris-virginica', 'category'] = 1
df['category'] = df['category'].astype('int')

print df.head()
print df.shape
print df.dtypes
# 取其中两个特征，即：花瓣长度，花瓣宽度，即第2列和第3列

X = df[['petal_length', 'petal_width']].values
y = df[['category']].values

X_std = np.c_[np.ones((df.shape[0], 1)), min_max(X)]

X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.2, random_state=0)
print X_train.shape
print X_test.shape

cost_record, theta, iters = logistic_regression(X_train, y_train)
print '----------------训练结果-------------------'
print "代价函数数组：", cost_record
print "theta参数：", theta
print "迭代次数：", iters

print '-----------------测试-----------------'
train_right_counts = 0
for i in range(X_train.shape[0]):
    original_val = y_train[i, :]
    predict_val = predict(theta, X_train[i, :])
    # print "Original:", original_val, " Predict:", predict_val, ("o" if original_val == predict_val else "x")
    if original_val == predict_val:
        train_right_counts += 1

print "训练集准确率：", ((train_right_counts * 1.0) / X_train.shape[0])

test_right_counts = 0
for i in range(X_test.shape[0]):
    original_val = y_test[i, :]
    predict_val = predict(theta, X_test[i, :])
    # print "Original:", original_val, " Predict:", predict_val, ("o" if original_val == predict_val else "x")
    if original_val == predict_val:
        test_right_counts += 1

print "测试集准确率：", ((test_right_counts * 1.0) / X_test.shape[0])

# 代价函数值收敛趋势图
plt.plot(np.arange(len(cost_record)-1), cost_record[1:], 'r')
plt.show()
