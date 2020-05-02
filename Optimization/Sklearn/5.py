from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt

###生成的数据如下图所示###
plt.figure
X,y=make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,             random_state=22,n_clusters_per_class=1,scale=100)
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()

###利用minmax方式对数据进行规范化###
X=preprocessing.minmax_scale(X)#feature_range=(-1,1)可设置重置范围
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
clf=SVC()
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))
#0.933333333333
#没有规范化之前我们的训练分数为0.511111111111,规范化后为0.933333333333,准确度有很大提升
