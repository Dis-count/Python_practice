import numpy as np
X = np.array([
                      [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],
                      [4,5,5,4,4,4,5,5,6,6,6,5,5,6,6]
             ])
X = X.T
y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])

nb = MultinomialNB(alpha=1.0,fit_prior=True)
nb.fit(X,y)
print nb.predict(np.array([2,4]))#输出-1
