# 交叉验证
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

###引入数据###
iris=load_iris()
X=iris.data
y=iris.target

###训练数据###
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
#引入交叉验证,数据分为5组进行训练
from sklearn.model_selection import cross_val_score
knn=KNeighborsClassifier(n_neighbors=5)#选择邻近的5个点
scores=cross_val_score(knn,X,y,cv=5,scoring='accuracy')#评分方式为accuracy
print(scores)#每组的评分结果
#[ 0.96666667  1\.          0.93333333  0.96666667  1\.        ]5组数据
print(scores.mean())#平均评分结果
#0.973333333333
